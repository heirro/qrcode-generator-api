from typing import Union
import qrcode
import io
import urllib.parse
import datetime

from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class QRCodeResponse(BaseModel):
    base64: str

app = FastAPI(
    title="QR Code Generator API",
    description="""
    Generate high-quality QR codes for websites, text, contact info or any data. 
    Free QR code API with customizable size and margins.
    Easy to use for developers, perfect for websites, applications, and marketing materials.
    No registration required.
    """,
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
)

@app.get(
    "/api/create/",
    summary="Create Custom QR Code Images Instantly",
    description="""
    Generate a QR code image from any text or URL with customizable parameters.
    Perfect for websites, business cards, marketing materials, and more.
    Returns a high-quality PNG image that can be saved or displayed directly.
    Data is automatically URL-encoded for compatibility.
    """,
    response_description="A PNG image of your generated QR code, ready to use",
)
async def generate_qrcode(
    data: str = Query(
        ..., 
        description="Text or URL to encode in the QR code. Can contain website links, contact information, or any text. Will be automatically URL-encoded.",
        example="https://example.com"
    ), 
    margin: int | None = Query(
        None, 
        description="Margin around the QR code (border width). Default is 1 if not specified.",
    ), 
    size: str | None = Query(
        None, 
        description="Size of the QR code. Can be 'S' (small), 'M' (medium), or 'L' (large). Default is 'M' if not specified.",
    ),
    error_level: str | None = Query(
        None,
        description="Error correction level. L (Low, 7% recovery), M (Medium, 15% recovery), Q (Quartile, 25% recovery), H (High, 30% recovery). Default is M if not specified.",
    )
):
    margin = 1 if not margin else margin
    
    if not size:
        box_size = 10
    elif size.upper() == "S":
        box_size = 5
    elif size.upper() == "M":
        box_size = 10
    elif size.upper() == "L":
        box_size = 15
    else:
        box_size = 10
        
    if not error_level:
        error_correction = qrcode.constants.ERROR_CORRECT_M
    elif error_level.upper() == "L":
        error_correction = qrcode.constants.ERROR_CORRECT_L
    elif error_level.upper() == "M":
        error_correction = qrcode.constants.ERROR_CORRECT_M
    elif error_level.upper() == "Q":
        error_correction = qrcode.constants.ERROR_CORRECT_Q
    elif error_level.upper() == "H":
        error_correction = qrcode.constants.ERROR_CORRECT_H
    else:
        error_correction = qrcode.constants.ERROR_CORRECT_M
    
    # URL encode the data
    #encoded_data = urllib.parse.quote(data)
    
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        border=margin,
        box_size=box_size
    )

    qr_code.add_data(data)
    qr_code.make(fit=True)

    img = qr_code.make_image(fill_color="black", back_color="white")

    img_buffer = io.BytesIO()
    img.save(img_buffer)
    img_buffer.seek(0)
    
    # Generate timestamp for filename
    timestamp = datetime.datetime.now().timestamp()
    filename = f"{timestamp}_qrcode.png"
    
    return StreamingResponse(
        img_buffer, 
        media_type="image/png",
        headers={
            "Content-Disposition": f"inline; filename={filename}",
            "Cache-Control": "max-age=86400"
        }
    )
