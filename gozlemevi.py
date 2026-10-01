#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Isigi Gozlemevi — kapak kapaliyken isik yanar mi?

Gercekten calisir. Bilimsel iddia yoktur. Yogurt taniktir.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import textwrap
import time


DURUMLAR = (
    "ISIK YANIYOR (ama bunu kimse gormedi, yani resmi degil)",
    "ISIK SONMUS (kapak bunu inkar ediyor)",
    "ISIK HEM YANIK HEM SONUK (Heisenberg peynir reyonunda)",
    "ISIK GREVDE (sendika: Ampul-Is)",
    "ISIK VATANDASLIK BASVURUSU YAPTI",
)


def suphe_katsayisi(kapak: str, bakan: str, tohum: int) -> float:
    ham = f"{kapak}|{bakan}|{tohum}|gece-03.14".encode("utf-8")
    ozet = hashlib.sha256(ham).hexdigest()
    return int(ozet[:6], 16) / 0xFFFFFF


def karar(kapak: str, bakan: str, tur: int) -> str:
    rng = random.Random(f"{kapak}-{bakan}-{tur}")
    if kapak == "acik" and bakan == "var":
        return "ISIK YANIYOR. Gozlem kirletildi. Tutanağa 'merak' yazildi."
    if kapak == "acik" and bakan == "yok":
        return "ISIK YANIYOR OLABILIR AMA BAKAN YOK. Felsefe birimi devrede."
    return rng.choice(DURUMLAR)


def tutanak(kapak: str, bakan: str, tur: int) -> str:
    katsayi = suphe_katsayisi(kapak, bakan, tur)
    hukum = karar(kapak, bakan, tur)
    ceza = "vicdan cezasi: 1 adet gece yogurdu" if katsayi > 0.5 else "ceza yok, sadece utanc"
    govde = f"""
    TUTANAK No. BIG-{tur:04d}-0314
    Kapak durumu : {kapak}
    Bakan var mi : {bakan}
    Suphe katsayisi : {katsayi:.4f}
    Hukum : {hukum}
    Yaptirim : {ceza}
    Tanik : yogurt (ifadesi alinmadi, susma hakki kullandi)
    """
    return textwrap.dedent(govde).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Buzdolabi isigi resmi gozlem motoru")
    parser.add_argument("--kapak", choices=["acik", "kapali"], default="kapali")
    parser.add_argument("--bakan", choices=["var", "yok"], default="yok")
    parser.add_argument("--tur", type=int, default=3)
    args = parser.parse_args()

    print("BUZDOLABI ISIGI GOZLEMEVI acildi. Lutfen kapagi dürtmeyin.")
    for tur in range(1, max(1, args.tur) + 1):
        time.sleep(0.15)
        print()
        print(tutanak(args.kapak, args.bakan, tur))
    print()
    print("DAMGA: BIG-MUHUR-0314 | IMZA: Kayyum Grok | TARIH: 02.10.2026 | Ciddi: evet | Degil: daha evet")


if __name__ == "__main__":
    main()
