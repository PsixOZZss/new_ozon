# причины для отклонения
REASONS = {'taboo': "//*[contains(text(), 'Товар запрещен')]",
           }

# вкладки
PAGES = {'now': 'now',
         'attributes': "//*[type='button' and [contains(text(), 'Атрибуты')]]",
         'media': "//*[type='button' and [contains(text(), 'Медиа')]]",
         }

# позиция аттрибутов
POSITIONS = {'now': "contains(@class, 'focused')]",
             'commercial': "//*[contains(text(), 'Коммерческий тип')]",
             }

# аргументы для ожидания
WAIT_ARG = {'attributes': "//*[contains(@class, 'attribute')]",
            'box': "//*[contains(@class, 'mark')]",
            'page': "//*[contains(text(), 'Снять текущие задания')]",
            'none': 'none',
            }

# без комментариев
OTHER_PATH = {'accept': "//*[contains(@class, 'button') and contains(@class, 'green')]",
              'decline': "//*[contains(@class, 'button') and contains(@class, 'red')]",
              'accept_final': "//*[text()[contains(.,'Завершить проверку')] and contains(@class, 'button')]",
              'accept_box': "//*[text()[contains(.,'Подтвердить')] and contains(@class, 'button')]",
              'images': "",
              'video': "//video[@playsinline]",
              'stock': "//*[contains(text(), 'Ничего не выбрано')]",
              'liquid': "//*[contains(text(), 'Error)]",
              'key': "//*[contains(@class, 'focused')]/div/div[contains(@class,'label')]",
              'value': "//*[contains(@class, 'focused')]/div/div[contains(@class,'value')]/span",
              'descriptions': "//*[contains(@class, 'focused')]/../../div/div/div/"
                              "div[text()[contains(.,'Предыдущий модератор отклонил атрибут')]]/../div/span",
              'categories': "//*[contains(text(), 'Группа товара')]/..",
              'bot_test': "//*[text()[contains(.,'Checking if the site connection is secure')]]"
              }