# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender suggests top songs from a small catalog based on user taste.
It is designed for classroom learning and experimentation.

**Intended use:**
- Explore how recommendation scoring works.
- Test how profile changes affect outputs.

**Non-intended use:**
- Not for real user personalization.
- Not for high-stakes decisions or mental health advice.
- Not for commercial deployment.

---

## 3. How the Model Works  

The model checks each song one by one. It gives points for genre match, mood match, and energy closeness. It also gives a small bonus when the user likes acoustic songs and the song is acoustic. After scoring all songs, it sorts them and returns the top `k`.

---

## 4. Data  

The catalog currently has 18 songs. Each song includes: `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. I expanded the starter dataset by adding more genres and moods. The data is still small, so many real music styles and listener contexts are missing.

---

## 5. Strengths  

The model is easy to understand because each recommendation has reasons. It works well for clear profiles like Chill Lofi and Deep Intense Rock. The top results usually match the user’s requested vibe.

---

## 6. Limitations and Bias 

The model can create a filter bubble. It may over-reward exact genre and mood matches and repeat similar songs. For unusual profiles (like unknown genre), it relies heavily on energy closeness that can produce songs that match numbers but do not fully match style.

---

## 7. Evaluation  

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Conflicted High-Energy Sad, and Unknown Genre + Chill + Very Low Energy. I compared whether each top-5 list changed in a meaningful way when preferences changed. I also ran a weight-shift experiment (higher energy weight, lower genre weight) to check sensitivity. A key surprise was how often `Gym Hero` stays near the top for happy pop users because it earns strong genre plus energy points.

---

## 8. Future Work  

1. Add diversity rules so top results are not too similar.
2. Support multi-genre and multi-mood user preferences.
3. Learn feature weights from feedback instead of fixed manual weights.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how one weight change can reorder the top songs fast. I expected small tuning to make small differences, but it changed the feel of recommendations a lot. AI tools helped me move faster when writing code, testing profiles, and improving documentation. I still had to double-check AI output, especially around Mermaid formatting, import paths, and whether results really matched my intent. What surprised me most is that a simple point system can still feel personal when the reasons are shown clearly. If I extend this project, I would add diversity rules, multi-preference profiles, and a feedback loop that learns better weights from user choices.
