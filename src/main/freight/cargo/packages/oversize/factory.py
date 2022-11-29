from src.main.freight.cargo.packages.oversize.builder \
    import OversizeOptionsBuilder

from src.main.freight.cargo.packages.oversize.interface import OversizeOptions


def normal_option_only() -> OversizeOptions:
    builder = OversizeOptionsBuilder()
    builder.add_option("normal", 1)

    return builder.build()


def full_options() -> OversizeOptions:
    builder = OversizeOptionsBuilder()
    builder.add_option("normal", 1)
    builder.add_option("oversize", 1.5)
    builder.add_option("double", 2)
    builder.add_option("triple", 3)

    return builder.build()
