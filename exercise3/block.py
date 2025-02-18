from sqlite3 import Time
from time import time
from typing import List

from exercise2.transaction_registry import Transaction
from simple_cryptography import hash


class Block:
    """
    Blok powinien zawierać:
    - hash poprzedniego bloku,
    - moment w czasie, w którym został stworzony,
    - listę transakcji
    - nonce.
    """

    prev_block_hash: bytes
    timestamp: int
    nonce: int
    transactions: List[Transaction]

    def __init__(
        self, prev_block_hash: bytes, transactions: List[Transaction], nonce: int = 0
    ):
        """
        TODO: Stwórz blok z podanych argumentów.
            Aby pobrać aktualny czas, użyj funkcji time(), a następnie zrzutuj ją na int'a ( int(time()) ).
        """
        # raise NotImplementedError()
        self.prev_block_hash = prev_block_hash
        self.timestamp = int(time())
        self.nonce = nonce
        self.transactions = transactions

    def hash(self) -> bytes:
        """
        TODO: Oblicz hash bloku wykorzystując do tego funkcję `hash` z modułu simple_cryptography.
            Hash powinien zostać obliczony ze skonkatenowanych składowych bloku:
            - prev_block_hash
            - timestamp
            - nonce
            - hasha wszystkich transakcji:
                - stwórz zmienną reprezentującą hash wszystkich transakcji (zainicjalizowaną bajtem zerowym b'\x00')
                - przechodząc po wszystkich transakcjach, zaktualizuj hash wszystkich transakcji hashem aktualnej
                 all_tx_hash = hash(all_tx_hash + current_tx_hash)
            Możesz założyć, że zarówno timestamp jak i nonce zajmują maksymalnie 32 bajty.
        """
        # raise NotImplementedError()
        hashed_txs = b'\x00'
        for transaction in self.transactions:
            hashed_txs = hash(hashed_txs + transaction.hash)

        return hash(
            self.prev_block_hash
            + self.timestamp.to_bytes(32, "big")
            + self.nonce.to_bytes(32, "big")
            + hashed_txs
        )
