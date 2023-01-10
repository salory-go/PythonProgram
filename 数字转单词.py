d = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
     '8': 'Eight', '9': 'Nine', '.': 'Point'}
while True:
    Str = input('enter a number:')
    try:
        Float = float(Str)
    except:
        print("\"{}\" is not a valid number.Please try again.".format(Str))
        continue
    if ',' in Str:
        print("Please try again without entering commas.")
    else:
        try:
            num = int(Str)
        except:
            Str = str(Float)
            print("As Text:", end=' ')
            if Float < 0:
                print('Negative', end=' ')
            for i in Str:
                print(d.get(i), end=' ')
            break
        Str = str(num)
        print("As Text:", end=' ')
        if num < 0:
            print('Negative', end=' ')
        for i in Str:
            print(d.get(i), end=' ')
        break