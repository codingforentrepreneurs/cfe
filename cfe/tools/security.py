# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_new_secrets.ipynb (unless otherwise specified).

__all__ = ['get_new_secret']

# Cell

import secrets

def get_new_secret(length:int = 32):
    if not isinstance(length, int):
        raise Exception(f"{length} is invalid. Please us a number")
    return secrets.token_urlsafe(length)