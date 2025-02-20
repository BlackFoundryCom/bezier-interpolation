# Bézier-interpolations


This repository demonstrates how to get Bézier interpolations (as opposed to linear interpolation) out of several layers of a single glyph.

1. Draw the initial state of the glyph.
2. Draw the final state of the glyph.
3. Draw the intermediate (target) state of the glyph (e.g. at time = 1/2)
    (For quadratic, there is only one step; for cubic there are two).

## FONTRA - How to do

For now the Fontra script only makes quadratic Bézier interpolations.

1. Set up your virtual environment
    ```sh
    cd your/repository/folder
    source setupvenv.sh
    ```
2. Run the script in your terminal by referencing the name of your glyph and the names of the start / target / stop layers:
    ```sh
    time python Fontra/fontra_bezier_interpolations.py --glyphName yourGlyphName --t timeValue --defaultSource nameOfYourDefaultSource --targetSource nameOfYourTargetSource --endSource nameOfYourEndSource --offSource1 nameOfYourOffSource1 --offSource2 nameOfYourOffSource2 your/font/path
    ```


## ROBOFONT - How to do


4. Generate the offset layers using the appropriate functions call
5. Set up your design space as llustrated below
6. Moving together the 2 axes (3 axes for Cubic) will generate the Bézier interpolation 


DESIGN SPACE FOR QUADRATIC BEZIER INTERPOLATION:

    glyphOff  -------------------- glyphEnd
      
     |                                | 
     
     |                                |
     
     |          (glyphTarget)         | 
     
     |                                |
     
     |                                |
     
    glyphStart --------------------  glyphOff


DESIGN SPACE FOR CUBIC BEZIER INTERPOLATION:

                glyphOff2  ------------------- glyphEnd
                    
                  |                                | 
                     
                  |                                |
                            (glyphTarget2)                     
                  |                                | 
                     
                  |                                |
                     
                  |                                |
                 
                glyphOff2 ---------------------  glyphOff2
    
                   /     
     
    glyphOff1  --/---------------- glyphOff1
    
     |         /                      | 
     
     |       /                        |
                (glyphTarget1)
     |     /                          | 
     
     |   /                            |
     
     | /                              |
       
    glyphStart --------------------  glyphOff1
