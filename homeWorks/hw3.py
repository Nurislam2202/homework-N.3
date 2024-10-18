class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        while True:
            try:
                self._balance += int(input(f'Введите сумму которую хотите добавить: '))
                break
            except ValueError:
                print('Введите цифры!')

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other):
        self._balance += other._balance

    def show_balance(self):
        print(f'На вашем балансе: {self._balance}')


client1 = Bank('Nurislam', 10_000)
client2 = Bank('Atabek', 100_000)
