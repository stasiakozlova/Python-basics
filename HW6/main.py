import sys
from collections import Counter

from github_user import GitHubUser


def select_one_username_from_input(users: list[GitHubUser]) -> GitHubUser:
    print("Пожалуйста, введите число, соответствующее номеру пользователя в списке ниже")

    for i, user in enumerate(users):
        print(f"{i+1}. {user.username}")

    while True:
        try:
            number = int(input())

            if (number < 1) or (number > len(users)):
                print("Введено некорректное число, попробуйте еще раз")
                continue

            return users[number - 1]

        except:
            print("Возникла ошибка при обработке, попробуйте еще раз")


def print_user_detailed_info(users: list[GitHubUser]):
    print("\n")

    user = select_one_username_from_input(users)

    print("Репозитории пользователя", user.username)

    for repo in user.repos:
        print(f"Название репозитория: {repo.name}. Описание репозитория: {repo.description}")

    print("\nЯзыки пользователя", user.username)

    for language, number_of_usages_in_repos in user.languages.most_common():
        print(language, number_of_usages_in_repos)


def print_stats(users: list[GitHubUser]):
    print("\n")

    sorted_by_number_of_repos = sorted(users, key=lambda user: user.number_of_repos, reverse=True)
    print("Больше всего репозиториев у:", sorted_by_number_of_repos[0].username)

    sorted_by_number_of_followers = sorted(users, key=lambda user: user.number_of_followers, reverse=True)
    print("Больше всего подписчиков у:", sorted_by_number_of_followers[0].username)

    counter = Counter()
    for user in users:
        counter += user.languages

    print("Самый популярный язык среди выбранных пользователей:", counter.most_common()[0][0])


def main():
    usernames = sys.argv[1:]

    if len(usernames) == 0:
        raise Exception("Нужно ввести как минимум один username")

    users = list(map(lambda username: GitHubUser(username), usernames))

    print_user_detailed_info(users)
    print_stats(users)


if __name__ == '__main__':
    main()
