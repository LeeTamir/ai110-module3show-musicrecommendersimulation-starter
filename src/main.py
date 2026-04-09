"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.88, "likes_acoustic": False}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.92, "likes_acoustic": False}),
        (
            "Edge Case: Conflicted High-Energy Sad",
            {"genre": "pop", "mood": "sad", "energy": 0.90, "likes_acoustic": False},
        ),
        (
            "Adversarial: Unknown Genre + Chill + Very Low Energy",
            {"genre": "k-pop", "mood": "chill", "energy": 0.05, "likes_acoustic": True},
        ),
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n=== Top Recommendations ===")
        print(f"Profile Name: {profile_name}")
        print(
            f"Profile: genre={user_prefs['genre']} | mood={user_prefs['mood']} | "
            f"energy={user_prefs['energy']:.2f} | likes_acoustic={user_prefs['likes_acoustic']}\n"
        )

        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            reason_items = [part.strip() for part in explanation.split(";") if part.strip()]

            print(f"{index}. {song['title']} — {song['artist']}")
            print(f"   Score: {score:.2f}")
            print("   Reasons:")
            for reason in reason_items:
                print(f"   - {reason}")
            print()


if __name__ == "__main__":
    main()
