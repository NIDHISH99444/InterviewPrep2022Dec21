
from typing import List, Dict

class User:
    user_id: str
    name: str
    email: str
    user_balance_mapping: Dict[str, int]
    expenses = List[int]


    def __init__(self, user_id: str, name: str, email: str, expenses: List[int] = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.user_balance_mapping = {}
        self.expenses = expenses

    def show_expense(self):
        formatted_output = []
        for user_id, amount in self.user_balance_mapping.items():
            if amount < 0:
                formatted_output.append(f'{self.user_id} owes {user_id}: {-amount}')
            elif amount > 0:
                formatted_output.append(f'{user_id} owes {self.user_id}: {amount}')
        if formatted_output:
            print('\n'.join(formatted_output))
        else:
            print('No balances')
        print()



class Expense:
    total_amount: int
    paid_by: User
    user_shares: Dict[User, int]

    def __init__(self, paid_by: User, total_amount: int, user_shares):
        self.paid_by = paid_by
        self.total_amount = total_amount
        self.user_shares = user_shares

    def update_user_calculation(self):
        """
        Update each user's user-balance-mapping to update consolidated data
        """
        for user, amount in self.user_shares.items():
            # user.add_expense(self)
            if user != self.paid_by:
                # Update  paid by user mapping
                print("paid user mapping",self.paid_by.user_balance_mapping)
                if user.user_id in self.paid_by.user_balance_mapping:
                    self.paid_by.user_balance_mapping[user.user_id] += amount
                else:
                    self.paid_by.user_balance_mapping[user.user_id] = amount

                # Update other participants mapping
                print("lend user mapping",user.user_balance_mapping)
                if self.paid_by.user_id in user.user_balance_mapping:
                    user.user_balance_mapping[self.paid_by.user_id] -= amount
                else:
                    user.user_balance_mapping[self.paid_by.user_id] = -amount


class UserService:
    users: Dict[str,User]


    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name='', email=''):
        if user_id in self.users:
            raise UserAlreadyExist()
        user = User(user_id, name, email)
        self.users[user.user_id] = user
        return user

    def get_or_add_user(self, user_id, name='', email=''):
        user = self.users.get(user_id)
        if not user:
            user = self.add_user(user_id, name, email)
        return user

    def show_expense(self):
        formatted_output = []
        for user in self.users.values():
            user_output = []
            for user_id, amount in user.user_balance_mapping.items():
                if amount < 0:
                    user_output.append(f'{user.user_id} owes {user_id}: {-amount}')
                elif amount > 0:
                    user_output.append(f'{user_id} owes {user.user_id}: {amount}')
            if user_output:
                formatted_output.append(f'{user.user_id} Expense data')
                formatted_output.extend(user_output)
        if formatted_output:
            print('\n'.join(formatted_output))
        else:
            print('No balances')
        print()




EXACT = 'EXACT'
EQUAL = 'EQUAL'

class ExpenseService:

    @staticmethod
    def add_equal_expense(paid_by, total_amount, participants):
        users_shares = {}
        total_participants = len(participants)
        # Calculate share of each user
        for index in range(total_participants):
            user = user_service.get_or_add_user(participants[index])
            users_shares[user] = total_amount / total_participants

        expense = Expense(
            user_service.get_or_add_user(paid_by),
            total_amount,
            users_shares
        )
        expense.update_user_calculation()

    @staticmethod
    def add_exact_expense(paid_by, total_amount, participants, shares: List[int]):
        users_shares = {}
        total_participants = len(participants)

        if total_amount == sum(shares):
            for index in range(total_participants):
                user = user_service.get_or_add_user(participants[index])
                users_shares[user] = shares[index]
        else:
            raise InValidAmount()

        expense = Expense(
            user_service.get_or_add_user(paid_by),
            total_amount,
            users_shares
        )
        expense.update_user_calculation()

#



class InValidAmount(Exception):
    message = 'Total amount and user shares are not matching'


class UserAlreadyExist(Exception):
    message = 'User already exists'


user_service = UserService()
user_service.show_expense()
user_service.get_or_add_user('user1').show_expense()
expense_service = ExpenseService()
expense_service.add_equal_expense('user1', 1000, ['user1', 'user2', 'user3', 'user4'])
user_service.get_or_add_user('user4').show_expense()
user_service.get_or_add_user('user1').show_expense()
expense_service.add_exact_expense('user1', 1250, ['user2', 'user3'], [370, 880])
user_service.show_expense()
expense_service.add_exact_expense('user4', 880, ['user3'], [880])
# user_service.get_or_add_user('user1').show_expense()
user_service.show_expense()