* Changed `Augmenter.augment_polygons()` to copy the augmenter's RNG
  before starting concave polygon recovery. This is done for cleanliness and
  should not have any effects for users. #447
* Removed RNG copies in `_ConcavePolygonRecoverer` to improve performance. #447
