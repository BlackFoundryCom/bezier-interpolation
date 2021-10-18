import math
from fontMath import mathGlyph

def quadraticInverse(glyphName, t, startLayer, stepLayer, endLayer, offLayer):
    mathG = mathGlyph.MathGlyph
    f = CurrentFont()
    g = f[glyphName].getLayer(startLayer)
    gStep = f[glyphName].getLayer(stepLayer)
    gEnd = f[glyphName].getLayer(endLayer)
    gOff = f[glyphName].getLayer(offLayer)

    mg = mathG(g)
    mgStep = mathG(gStep)
    mgEnd = mathG(gEnd)

    k = 1-t

    gOff.clear()
    mgOff = (mgStep - k*k*mg - t*t*mgEnd)/(t*k*2)
    pen = gOff.getPen()
    mgOff.draw(pen, filterRedundantPoints=True)

def cubicInverse(glyphName, t1, t2, startLayer, step1Layer, step2Layer, endLayer, off1Layer, off2Layer):
    mathG = mathGlyph.MathGlyph
    f = CurrentFont()
    g = f[glyphName].getLayer(startLayer)
    gStep1 = f[glyphName].getLayer(step1Layer)
    gStep2 = f[glyphName].getLayer(step2Layer)
    gEnd = f[glyphName].getLayer(endLayer)
    gOff1 = f[glyphName].getLayer(off1Layer)
    gOff2 = f[glyphName].getLayer(off2Layer)

    mg = mathG(g)
    mgStep1 = mathG(gStep1)
    mgStep2 = mathG(gStep2)
    mgEnd = mathG(gEnd)

    k1 = 1-t1
    k2 = 1-t2

    mg1 = (mgStep1 - k1*k1*k1*mg - t1*t1*t1*mgEnd)/3
    mg2 = (mgStep2 - k2*k2*k2*mg - t2*t2*t2*mgEnd)/3
    denom = k1*t2-t1*k2
    mgOff1 = ((t2/(k1*t1))*mg1 - (t1/(k2*t2))*mg2)/denom
    mgOff2 = (((-k2)/(k1*t1))*mg1 + (k1/(k2*t2))*mg2)/denom

    gOff1.clear()
    mgOff1.draw(gOff1.getPen(), filterRedundantPoints=True)

    gOff2.clear()
    mgOff2.draw(gOff2.getPen(), filterRedundantPoints=True)


# Tests:
quadraticInverse("A", 0.5, "foreground", "quadratictarget", "end", "quadraticoff")
cubicInverse("A", 1/3, 2/3, "foreground", "cubictarget1", "cubictarget2", "end", "cubicoff1", "cubicoff2")
