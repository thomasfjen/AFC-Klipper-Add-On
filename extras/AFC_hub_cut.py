import chelper
from . import AFC

class afc_hubcut:
    def __init__(self, config):
<<<<<<< Updated upstream
        self.AFC = AFC.afc
=======
        self.printer = config.get_printer()
        self.name = config.get_name().split()[-1]
        self.AFC = self.printer.lookup_object('AFC')2
        self.gcode = self.printer.lookup_object('gcode')
        self.reactor = self.printer.get_reactor()
>>>>>>> Stashed changes

        #HUB cut_sizeself.hub_cut_active = config.getboolean("hub_cut_active", False)
        self.AFC = self.printer.lookup_object('AFC')
        self.hub_cut_dist = config.getfloat("hub_cut_dist", 200)
        self.hub_cut_clear = config.getfloat("hub_cut_clear", 120)
        self.hub_cut_min_length = config.getfloat("hub_cut_min_length", 200)
        self.hub_cut_servo_pass_angle = config.getfloat("hub_cut_servo_pass_angle", 0)
        self.hub_cut_servo_clip_angle = config.getfloat("hub_cut_servo_clip_angle", 160)
        self.hub_cut_servo_prep_angle = config.getfloat("hub_cut_servo_prep_angle", 75)
        self.hub_cut_confirm = config.getfloat("hub_cut_confirm", 0)

<<<<<<< Updated upstream
    def hub_cut(self, CUR_LANE):
=======
    def hub_cut(self, LANE):
        CUR_LANE = self.printer.lookup_object('AFC_stepper ' + LANE)
        self.hub = self.printer.lookup_object('filament_switch_sensor ' + self.name).runout_helper
>>>>>>> Stashed changes
        # Prep the servo for cutting.
        self.gcode.run_script_from_command('SET_SERVO SERVO=cut ANGLE=' + str(self.hub_cut_servo_prep_angle))
        # Load the lane until the hub is triggered.
        while self.hub.filament_present == False:
            CUR_LANE.move( self.hub_move_dis, self.short_moves_speed, self.short_moves_accel)
        # Go back, to allow the `hub_cut_dist` to be accurate.
        CUR_LANE.move( -self.hub_move_dis*4, self.short_moves_speed, self.short_moves_accel)
        # Feed the `hub_cut_dist` amount.
        CUR_LANE.move( self.hub_cut_dist, self.short_moves_speed, self.short_moves_accel)
        # Have a snooze
        # Choppy Chop
        self.gcode.run_script_from_command('SET_SERVO SERVO=cut ANGLE=' + str(self.hub_cut_servo_clip_angle))
        if self.hub_cut_confirm == 1:
            # ReChop, To be doubly choppy sure.
            self.gcode.run_script_from_command('SET_SERVO SERVO=cut ANGLE=' + str(self.hub_cut_servo_prep_angle))
            self.gcode.run_script_from_command('SET_SERVO SERVO=cut ANGLE=' + str(self.hub_cut_servo_clip_angle))
        # Longer Snooze
        # Align bowden tube (reset)
        self.gcode.run_script_from_command('SET_SERVO SERVO=cut ANGLE=' + str(self.hub_cut_servo_pass_angle))
        # Retract lane by `hub_cut_clear`.
        CUR_LANE.move( -self.hub_cut_clear, self.short_moves_speed, self.short_moves_accel)

def load_config_prefix(config):
    return afc_hubcut(config)