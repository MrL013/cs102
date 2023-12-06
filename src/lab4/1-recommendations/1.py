from typing import List, Dict

class Recommendations_system:
    def __init__(self, films_pack: str, history_pack: str):
        self.films = self.check_films(films_pack)
        self.history = self.check_history(history_pack)

    def check_films(self, file_path: str) -> Dict[int, str]:
        with open(file_path, 'r', encoding='utf-8') as file:
            res_films = [film.split(',') for film in file.read().splitlines()]
            return {int(film[0]): film[1] for film in res_films}

    def check_history(self, file_path: str) -> List[List[int]]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [list(map(int, history.split(','))) for history in file.read().splitlines()]

    def recomendation_system(self, user_views: List[int]) -> str:
        search_users = []

        for user in self.history:
            all_views = set(user_views) and set(user)
            if len(all_views) >= len(user_views) / 2:
                search_users.append(user)
        
        watched_films = set(user_views)

        recomendations_films = {}

        for user in search_users:
            for film_id in user:
                if film_id not in watched_films and film_id in self.films:
                    recomendations_films[film_id] = recomendations_films.get(film_id, 0) + 1
        
        if recomendations_films:
            max_views = max(recomendations_films.values())
            for film_id, views in recomendations_films.items():
                if views == max_views:
                    return self.films[film_id]
        
        return 'no recomendation'

def main():
    data_films = 'files/films.txt'
    data_history = 'files/history.txt'

    recommendations = Recommendations_system(data_films, data_history)

    user_input = input()
    user_views = list(map(int, user_input.split(',')))

    recommendation_result = recommendations.recomendation_system(user_views)

    print('recomendation:', recommendation_result)

if __name__ == '__main__':
    main()