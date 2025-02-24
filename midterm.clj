(defn tetrahedron-volume [a]
  "Calculates the volume of a tetrahedron with side length a."
  (/ (* (Math/sqrt 2) (Math/pow a 3)) 12))

(defn is-close-to-integer? [value precision]
  "Checks if a value is within the given precision of an integer."
  (let [rounded (Math/round value)]
    (<= (Math/abs (- value rounded)) precision)))

(defn tetrahedron-volume-sum [start end precision]
  "Calculates the sum of integer-valued tetrahedron volumes within the given precision."
  (->> (range start (inc end)) ; Generate side lengths from start to end (inclusive)
       (map tetrahedron-volume) ; Calculate the volume for each side length
       (filter #(is-close-to-integer? % precision)) ; Filter volumes close to integers
       (map #(Math/round %)) ; Round the volumes to integers
       (reduce +))) ; Sum the rounded volumes

;; Example usage:
(println (tetrahedron-volume-sum 1 10 0.1))
;; Output: 87