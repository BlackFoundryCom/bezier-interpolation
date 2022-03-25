# bezier-interpolations
This python script for RoboFont demonstrates how to get Bezier interpolations (as opposed to linear interpolation) out of several layers of a single glyph.

## How to do
1. Draw the initial state of the glyph
2. Draw the final state of the glyph
3. Draw the intermediate (target) state of the glyph (e.g. at time = 1/2)
  (for quadratic there is only 1 step, for cubic there are 2)
4. Generate the offset layers using the appropriate functions call
5. Set up your design space as llustrated below
6. Moving together the 2 axes (3 axes for Cubic) will generate the Bezier interpolation 

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
                     
                  |                                | 
                     
                  |                                |
                     
                  |                                |
                 
                glyphOff2 ---------------------  glyphOff2
    
                   /     (glyphTarget)
     
    glyphOff1  --/---------------- glyphOff1
    
     |         /                      | 
     
     |       /                        |
     
     |     /                          | 
     
     |   /                            |
     
     | /                              |
       
    glyphStart --------------------  glyphOff1
