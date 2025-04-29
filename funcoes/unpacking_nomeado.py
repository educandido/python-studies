# **kwargs -> kew word args

def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    podium = {'primeiro':'F. Massa',
              'segundo':'Alonso',
              'terceiro':'Verstapen'}
    
    resultado_f1(**podium)
