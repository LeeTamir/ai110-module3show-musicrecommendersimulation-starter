# Reflection: Profile Comparisons

Profiles compared:
- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Edge Case: Conflicted High-Energy Sad
- Adversarial: Unknown Genre + Chill + Very Low Energy

## Pairwise Output Notes

- **High-Energy Pop vs Chill Lofi:** High-Energy Pop pushes tracks like `Sunrise City` and `Gym Hero`, while Chill Lofi shifts toward `Library Rain` and `Midnight Coding`. This makes sense because one profile rewards energetic pop mood and the other rewards chill mood plus acoustic texture.
- **High-Energy Pop vs Deep Intense Rock:** Both profiles like high-energy songs, but the rock profile lifts `Storm Runner` to #1 because it matches both rock and intense mood. The pop profile keeps `Sunrise City` higher because it matches pop and happy.
- **High-Energy Pop vs Conflicted High-Energy Sad:** `Gym Hero` stays very high in both lists because energy and genre are strong signals, even when mood is sad. This shows why `Gym Hero` keeps appearing for users who still ask for happy pop style energy.
- **High-Energy Pop vs Unknown Genre + Chill + Very Low Energy:** Pop-heavy songs drop and calmer tracks rise. That makes sense because the unknown genre gives no genre points, so mood and low-energy closeness drive results.

- **Chill Lofi vs Deep Intense Rock:** Chill Lofi favors softer songs with acoustic bonus, while Deep Intense Rock favors aggressive high-energy songs like `Storm Runner`. The lists separate clearly because the moods and energy targets are opposite.
- **Chill Lofi vs Conflicted High-Energy Sad:** The lofi profile chooses calm songs; the conflicted profile drifts toward intense tracks due to high energy. This suggests energy can overpower mood when there are few exact sad matches.
- **Chill Lofi vs Unknown Genre + Chill + Very Low Energy:** These two look similar at the top because both reward chill mood and lower energy. The main difference is that Chill Lofi gives extra points to lofi genre matches, while unknown genre cannot.

- **Deep Intense Rock vs Conflicted High-Energy Sad:** Both prefer high-energy songs, but the rock profile rewards rock/intense songs more directly. The conflicted profile loses mood-match power because “sad” is rare in this dataset.
- **Deep Intense Rock vs Unknown Genre + Chill + Very Low Energy:** Results flip from aggressive tracks to calm tracks. This is expected because both the mood and energy target are reversed.

- **Conflicted High-Energy Sad vs Unknown Genre + Chill + Very Low Energy:** Conflicted high-energy profiles still rank energetic tracks near the top, while unknown-genre chill profiles prioritize mood and low-energy songs. The difference makes sense and shows the scoring responds to user preference changes.

## Takeaway in Plain Language

The recommender is directionally valid: when I change preferences, the top songs usually change in the way I would expect. The biggest pattern is that high energy and exact genre matches can keep certain songs (like `Gym Hero`) near the top, even when mood is imperfect.
