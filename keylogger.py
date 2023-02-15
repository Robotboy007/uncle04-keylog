from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        if hasattr(key, 'vk') and 96 <= key.vk <= 105:
            print('result: ', int(key.vk)-96)
        with open('log.txt','a',encoding='utf') as file:
            t = '{}'.format(key.char)
            file.write(t)
    except AttributeError:
        print('special key {0} pressed'.format(key))
        with open('log.txt','a',encoding='utf') as file:
            t = '|{}|'.format(key)
            file.write(t)

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()