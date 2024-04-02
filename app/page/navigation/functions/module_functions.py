from ..builder import Module


def get_module(index: int) -> Module:
    return Module.all_modules[index]

def get_and_build_destinations() -> list:
    return [module.rail.build() for module in Module.all_modules]