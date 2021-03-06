from panda3d import core as p3d

from quest.engine import runtime

from dataclasses import dataclass

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

@dataclass
class TileVisualData(object):
    """
    """

    tile_x: int
    tile_y: int

    tile_count_x: int
    tile_count_y: int

    sheet: object

    rect: object
    flags: object

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def load_tiled_image(filename: str, colorkey: object, **kwargs) -> object:
    """
    """   
    
    filename = filename.replace('zones/devplanet\../../tsx\../', '')
    image_buffer = p3d.PNMImage(filename)

    def create_tile_visual_data(rect: object = None, flags: object = None) -> TileVisualData:
        """
        """
        
        x, y, w, h = rect
        tile_count_x = image_buffer.get_x_size() / w
        tile_count_y = image_buffer.get_y_size() / h

        tile_x = get_tile_coord(x, w, tile_count_x)
        tile_y = get_tile_coord(y, h, tile_count_y, invert=True)

        visual_data = TileVisualData(
            tile_x, tile_y,
            tile_count_x, tile_count_y,
            image_buffer,
            rect, 
            flags)

        return visual_data
    
    return create_tile_visual_data

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def get_tile_coord(pixel_start: int, pixel_size: int, tile_count: int, invert: bool = False) -> int:
    """
    """

    tile_coord = int(pixel_start / pixel_size)
    if invert: tile_coord = abs(tile_count - (tile_coord + 1))
    return int(tile_coord)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#