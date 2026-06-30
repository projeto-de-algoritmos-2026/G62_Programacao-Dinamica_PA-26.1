from datetime import datetime
from enum import Enum
from typing import Any

import weighted_interval_scheduling
from job import Job

class CliCommand(Enum):
    EXIT = 0
    SET_LIST = 1
    SHOW = 2

class Cli:
    def __init__(self):
        self.current_list: list[Job] = []
    
    @staticmethod
    def query_job(num: int) -> Job:
        # Ler 1 único Job com a mensagem msg
        retval: Job = []
        retval.start = datetime(input(f"\nEvento {num}\n\nDigite a data e hora de começo: "))

    @staticmethod
    def query_job_list(sizeMsg: str) -> list[Job]:
        size = int(input("Digite o tamanho da lista: "))
        retval: list[Job] = []
        for i in range(1, size + 1):
            retval.append(Cli.query_job(i))
        return retval