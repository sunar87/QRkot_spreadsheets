from datetime import datetime

from aiogoogle import Aiogoogle

from app.core import constants as const
from app.core.config import settings


SHEETS_API_VERSION = 'v4'
DRIVE_API_VERSION = 'v3'


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(const.FORMAT)
    service = await wrapper_services.discover('sheets', SHEETS_API_VERSION)
    spreadsheet_body = {
        'properties': {
            'title': const.SPREADSHEET_TITLE.format(now_date_time),
            'locale': const.LOCALE
        },
        'sheets': [
            {'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': const.SHEET_TITLE,
                'gridProperties': {'rowCount': const.ROW_COUNT,
                                   'columnCount': const.COLUMN_COUNT}
            }
            }
        ]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', DRIVE_API_VERSION)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields='id'
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        charity_projects: list,
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(const.FORMAT)
    service = await wrapper_services.discover('sheets', SHEETS_API_VERSION)
    table_values = [
        [const.A1, now_date_time],
        [const.A2],
        [const.A3, const.B3, const.C3]
    ]
    for project in charity_projects:
        new_row = [
            str(project.name),
            str(project.close_date - project.create_date),
            str(project.description)
        ]
        table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=const.RANGE,
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
