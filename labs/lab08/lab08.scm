(define (over-or-under num1 num2) 
    (if (< num1 num2)
    -1
    (if (= num1 num2) 0 1))
)

(define (composed f g) 
    (lambda (x) (f (g x)))
)

(define (square n) (* n n)
)

(define (pow base exp) 
    (if (= base 1)
        1
        (if (= exp 1)
            base
            (* base (pow base (- exp 1)))
        )
    )
)

(define (ascending? lst) 
    (if(eq? (cdr lst) nil)
        #t
        (if(> (car lst) (car (cdr lst)))
            #f
            (and #t (ascending? (cdr lst)))
        )
    )
)
