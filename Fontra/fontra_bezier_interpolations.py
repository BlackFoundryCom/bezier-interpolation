import argparse
import asyncio

from fontra.backends.fontra import FontraBackend


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--glyphName")
    parser.add_argument("--t")
    parser.add_argument("--defaultSource")
    parser.add_argument("--targetSource")
    parser.add_argument("--endSource")
    parser.add_argument("--offSource1")
    parser.add_argument("--offSource2")
    parser.add_argument("fontpath")

    args = parser.parse_args()

    pathToDesignspaceFile = args.fontpath

    font = FontraBackend.fromPath(pathToDesignspaceFile)
    glyphMap = await font.getGlyphMap()

    glyphName = args.glyphName
    glyph = await font.getGlyph(glyphName)

    startSource = args.defaultSource
    targetSource = args.targetSource
    endSource = args.endSource
    offSource = args.offSource1
    offSource2 = args.offSource2

    t = float(args.t)
    k = 1 - t

    off_coords = []

    gstart_coords = glyph.layers[startSource].glyph.path.coordinates
    gsteps_coords = glyph.layers[targetSource].glyph.path.coordinates
    gends_coords = glyph.layers[endSource].glyph.path.coordinates

    for start, step, end in zip(gstart_coords, gsteps_coords, gends_coords):
        p = (step - k * k * start - t * t * end) / (t * k * 2)
        off_coords.append(p)

    glyph.layers[offSource].glyph.path.coordinates = off_coords
    glyph.layers[offSource2].glyph.path.coordinates = off_coords

    print(f"- Save {glyphName}")
    error = await font.putGlyph(glyphName, glyph, glyphMap.get(glyphName, []))
    if error:
        print("!!!", glyphName, error)


if __name__ == "__main__":
    asyncio.run(main())
