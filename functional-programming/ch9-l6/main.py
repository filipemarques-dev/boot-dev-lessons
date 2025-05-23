from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):

    def pending_status(data):
        new_tuple = ("Pending...", list(map(lambda inner_list: list(map(str, inner_list)), data)))
        return new_tuple

    def processing_status(data):
        inner_result = list(map(lambda inner_list: ",".join(inner_list), data))
        new_tuple = ("Processing...", "\n".join(inner_result))
        return new_tuple

    def success_status(data):
        new_tuple = ("Success!", data)
        return new_tuple

    def failure_status(data):
        pending = pending_status(data)
        processing = processing_status(pending[1])
        new_tuple = ("Unknown error, retrying...", processing[1])
        return new_tuple
        
    match (status):
        case (CSVExportStatus.PENDING):
            return pending_status(data)
        case (CSVExportStatus.PROCESSING):
            return processing_status(data)
        case (CSVExportStatus.SUCCESS):
            return success_status(data)
        case (CSVExportStatus.FAILURE):
            return failure_status(data)
        case _:
            raise Exception("unknown export status")
