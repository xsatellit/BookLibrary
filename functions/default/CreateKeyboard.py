from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Keyboard:

    def getKeyboard(self, list_name: list, list_callb_data: list) -> InlineKeyboardMarkup:
        rows = []

        for callb, name in zip(list_callb_data, list_name):
            rows.append([InlineKeyboardButton(name, callback_data=callb)])

        keyboard = InlineKeyboardMarkup(inline_keyboard=rows)

        return keyboard

    def getKeyboardFromDict(self, list_dicts: list) -> InlineKeyboardMarkup:

        keyboard = InlineKeyboardMarkup(
            [[dictionary for dictionary in list_dicts]]
        )

        return keyboard

    def getKeyboardWithInSameLine(self, list_name: list, list_callb_data: list, list_inline: list, list_callb_data_inline: list) -> InlineKeyboardMarkup:
        rows = []

        for callb, name in zip(list_callb_data, list_name):
            rows.append([InlineKeyboardButton(name, callback_data=callb)])

        rows2 = []
        for callb, name in zip(list_callb_data_inline, list_inline):
            rows2.append(InlineKeyboardButton(name, callback_data=callb))
        rows.append(rows2)

        keyboard = InlineKeyboardMarkup(inline_keyboard=rows)

        return keyboard
    
    def getKeyboartInSameLine(self, list_name: list, list_callb: list):
        rows2 = []
        for callb, name in zip(list_callb, list_name):
            rows2.append(InlineKeyboardButton(name, callback_data=callb))

        keyboard = InlineKeyboardMarkup(inline_keyboard=[rows2])

        return keyboard