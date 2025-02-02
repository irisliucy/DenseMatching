class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = 'snapshots/'
        # Base directory for saving network checkpoints.
        self.tensorboard_dir = self.workspace_dir  # Directory for tensorboard files.
        self.pretrained_networks = self.workspace_dir 
        self.pre_trained_models_dir = ''
        self.megadepth = 'data/megadepth_test_set/MegaDepth/Test/test1600Pairs/'
        self.megadepth_csv = 'data/megadepth_test_set/MegaDepth/Test/test1600Pairs.csv'
        self.robotcar = 'data/RobotCar/'
        self.robotcar_csv = 'data/RobotCar/test6511.csv'
        self.hp = 'data/hpatches-sequences-release/'
        self.eth3d = 'data/ETH3D/'
        self.kitti2012 = 'data/KITTI_2012/training/'
        self.kitti2015 = 'data/KITTI_2015/training/'
        self.sintel = 'data/sintel/training/'
        self.yfcc = 'data/yfcc100m'
        self.tss = 'data/TSS_CVPR2016/'

