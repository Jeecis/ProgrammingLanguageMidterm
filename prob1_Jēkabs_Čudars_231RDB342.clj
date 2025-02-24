;; 231RDB342
;; For this task I relied on github copilot with /fix built in function 
;; and its code generation function
;; Furthermore I utilized t3.chat built by Youtuber Theo T3, to be able to use plethora of models
(defn icosahedron_volume_sum [start end precision]
  ;; Calculate the volume factor for the icosahedron
  (let [volume-factor (/ (* 5 (+ 3 (Math/sqrt 5))) 12) ;; calculates 5(3 + √5)/12
        ;; Fix the volume calculation function (It had few syntax errors, which github copilot fixed it)
    calculate-icosahedron-volume (fn [edge] (* volume-factor (Math/pow edge 3)))
        ;; Used Deepseek distilled in t3.chat querying "Why does my precision checking not work?"
    near-integer? (fn [x] (<= (Math/abs (- x (Math/round x))) precision))
    volumes (map (fn [edge] ;; Maps over edge lengths from start to end
                   ;; For each edge ...
             (let [vol (calculate-icosahedron-volume edge)] ;; Volume is calculated
         (when (near-integer? vol) ;; if volume is near an integer within a specific precision ...
           (Math/round vol)))) ;; The volume gets rounded
          ;; Asked google Gemini Flash model to apply the iteration in range
           (range start (inc end)))] ;; Iterates over the range of edges from start to end
      (reduce + 0 (remove nil? volumes)))) ;; Removes nil values that occur in Volumes function if number is not near integer


  (println (icosahedron_volume_sum 1 77 0.1))
  ;; Result 2310221