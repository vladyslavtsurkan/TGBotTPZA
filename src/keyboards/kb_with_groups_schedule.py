from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.models import Group


def get_keyboard_with_groups(groups: list[Group], function: str) -> InlineKeyboardMarkup:
    keyboard_with_groups = InlineKeyboardMarkup(row_width=2)
    for group in groups:
        keyboard_with_groups.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=f'{group.Department.title_short} ({group.Department.Faculty.title_short})',
                    callback_data=f'group schedule {function} {group.id}'
                )
            ]
        )

    return keyboard_with_groups
