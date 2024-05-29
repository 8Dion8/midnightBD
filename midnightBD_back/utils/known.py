class KnownComponentHandler:
    def __init__(self) -> None:
        self.knownPathMap = {
            'gpu': {
                'amd': 'configs/known_amd_gpu.txt',
                'nvidia': 'configs/known_nvidia_gpu.txt'
            }
        }
    def getKnown(self, component, brand):
        with open(self.knownPathMap[component][brand], 'r') as f:
            l = f.read().splitlines()
        return l