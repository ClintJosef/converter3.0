import PySimpleGUI as sg


def calculator_window(theme: str = None):
    if theme is not None:
        sg.theme(theme)
    sg.set_options(font='ComicSansMS 14', button_element_size=(2, 2))
    menu = ['menu', ['Purple', 'Tan', 'HotDogStand', 'GrayGrayGray', 'Dark', 'LightBlue1', 'DarkTeal2', 'random']]
    layout = [
        [sg.Text(
            'output',
            key='-NUM-',
            justification='right',
            p=(10, 20),
            font="ComicSansMS 25",
            right_click_menu=menu)],
        [sg.Button('Clear', expand_x=True), sg.Button('Delete', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(1, expand_x=True), sg.Button(2, expand_x=True), sg.Button(3, expand_x=True), sg.Button('/', expand_x=True)],
        [sg.Button(4, expand_x=True), sg.Button(5, expand_x=True), sg.Button(6, expand_x=True), sg.Button('*', expand_x=True)],
        [sg.Button(7, expand_x=True), sg.Button(8, expand_x=True), sg.Button(9, expand_x=True), sg.Button('-', expand_x=True)],
        [sg.Button(0, expand_x=True), sg.Button('.'), sg.Button('+')]]
    return sg.Window(
        'Calculator',
        layout,
        element_justification='right',
        return_keyboard_events=True
    )


def calculator():
    nums = []
    display_num = ''
    operations = []

    window = calculator_window()

    print("App started")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: break

        if event in ['Purple', 'Tan', 'HotDogStand', 'GrayGrayGray', 'Dark', 'LightBlue1', 'DarkTeal2', 'random']:
            window.close()
            window = calculator_window(event)

        if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            nums.append(event)
            display_num = ''.join(nums)
            window['-NUM-'].update(display_num)

        if event in ['*', '/', '-', '+']:
            operations.append(display_num)
            nums = []
            operations.append(event)
            window['-NUM-'].update('')

        if event == 'Enter':
            if operations:
                try:
                    operations.append(display_num)
                    result = eval(''.join(operations))
                    window['-NUM-'].update(result)
                except ZeroDivisionError:  # Did not know this error existed
                    operations = []
                    nums = []
                    window['-NUM-'].update("Can't divide by zero")  # But I can see why it does
            else: window['-NUM-'].update('At least enter something')

        if event == 'Clear':
            operations = []
            nums = []
            window['-NUM-'].update('output')

        if event == 'Delete':
            if display_num and nums:
                display_num = display_num[:-1]
                nums = nums[:-1]
                window['-NUM-'].update(display_num)
            else: window['-NUM-'].update('At least enter something')
    window.close()


if __name__ == '__main__':
    calculator()
