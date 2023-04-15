# Funkcje hashujące

from dataclasses import dataclass
from simple_cryptography import hash


@dataclass
class Transaction:
    id: int
    target_id: int
    metadata: str

    def hash(self) -> bytes:
        """
        TODO: zaimplementuj funkcję hashującą transakcje, wykorzystując funkcję hash z simple_cryptography.
            Wykorzystaj metodę int.to_bytes(2, 'big') oraz bytes(string, 'utf-8') do konwersji int to bytes.
            Bytes można konkatenować.
        """
        # raise NotImplementedError()
        return hash(
            int.to_bytes(self.id, 2, "big")
            + int.to_bytes(self.target_id, 2, "big")
            + bytes(self.metadata, "utf-8")
        )
