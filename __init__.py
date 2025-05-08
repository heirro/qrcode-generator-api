"""
QR Code Generator API Package

A simple API for generating QR codes with customizable properties.
"""

from .main import app, generate_qrcode

__version__ = "1.0.0"
__author__ = "Vava Heirro"
__all__ = [
    'app',              # The FastAPI application instance
    'generate_qrcode',  # The QR code generation function
]
