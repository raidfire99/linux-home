#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Radar Data Client
# Author: LFC
# Description: Client to receive processed radar data, providing live graphical feedback and recording of a datafile for offline processing
# Generated: Tue Jan  7 12:20:10 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class Radar_Data_Client(gr.top_block, Qt.QWidget):

    def __init__(self, parameter_0=149):
        gr.top_block.__init__(self, "Radar Data Client")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Radar Data Client")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Radar_Data_Client")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Parameters
        ##################################################
        self.parameter_0 = parameter_0

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1500000
        self.blocks_per_tag = blocks_per_tag = 2**17
        self.samp_per_freq = samp_per_freq = 1
        self.freq_res = freq_res = samp_rate/2/blocks_per_tag
        self.delta_freq = delta_freq = samp_rate/4
        self.center_freq = center_freq = 1000000000
        self.C = C = 299792458
        self.v_res = v_res = freq_res*3e8/2/center_freq
        self.samp_discard = samp_discard = 0
        self.min_output_buffer = min_output_buffer = 2*(blocks_per_tag*samp_per_freq*2)
        self.lo = lo = 2033000000
        self.fft_size = fft_size = 512
        self.decimator_fac = decimator_fac = 2**7
        self.decim = decim = 512
        self.WL = WL = C/samp_rate
        self.R_max = R_max = 3e8/2/delta_freq

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	fft_size, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_raster_sink_x_0_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	64,
        	fft_size,
        	([]),
        	([]),
        	"Mag",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_0.set_update_time(0.01)
        self.qtgui_time_raster_sink_x_0_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_raster_sink_x_0_0_win)
        self.fft_vxx_0_0_0_1 = fft.fft_vcc(fft_size, False, (window.blackmanharris(fft_size)), False, 8)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, fft_size)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, 'localhost', 3333, 1472, True)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'c:\\kandar\\RadarData\\radar.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(fft_size)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.fft_vxx_0_0_0_1, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.qtgui_time_raster_sink_x_0_0, 0))
        self.connect((self.fft_vxx_0_0_0_1, 0), (self.blocks_complex_to_mag_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Radar_Data_Client")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_parameter_0(self):
        return self.parameter_0

    def set_parameter_0(self, parameter_0):
        self.parameter_0 = parameter_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.set_freq_res(self.samp_rate/2/self.blocks_per_tag)
        self.set_delta_freq(self.samp_rate/4)
        self.set_WL(self.C/self.samp_rate)

    def get_blocks_per_tag(self):
        return self.blocks_per_tag

    def set_blocks_per_tag(self, blocks_per_tag):
        self.blocks_per_tag = blocks_per_tag
        self.set_min_output_buffer(2*(self.blocks_per_tag*self.samp_per_freq*2))
        self.set_freq_res(self.samp_rate/2/self.blocks_per_tag)

    def get_samp_per_freq(self):
        return self.samp_per_freq

    def set_samp_per_freq(self, samp_per_freq):
        self.samp_per_freq = samp_per_freq
        self.set_min_output_buffer(2*(self.blocks_per_tag*self.samp_per_freq*2))

    def get_freq_res(self):
        return self.freq_res

    def set_freq_res(self, freq_res):
        self.freq_res = freq_res
        self.set_v_res(self.freq_res*3e8/2/self.center_freq)

    def get_delta_freq(self):
        return self.delta_freq

    def set_delta_freq(self, delta_freq):
        self.delta_freq = delta_freq
        self.set_R_max(3e8/2/self.delta_freq)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.set_v_res(self.freq_res*3e8/2/self.center_freq)

    def get_C(self):
        return self.C

    def set_C(self, C):
        self.C = C
        self.set_WL(self.C/self.samp_rate)

    def get_v_res(self):
        return self.v_res

    def set_v_res(self, v_res):
        self.v_res = v_res

    def get_samp_discard(self):
        return self.samp_discard

    def set_samp_discard(self, samp_discard):
        self.samp_discard = samp_discard

    def get_min_output_buffer(self):
        return self.min_output_buffer

    def set_min_output_buffer(self, min_output_buffer):
        self.min_output_buffer = min_output_buffer

    def get_lo(self):
        return self.lo

    def set_lo(self, lo):
        self.lo = lo

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.qtgui_time_raster_sink_x_0_0.set_num_cols(self.fft_size)

    def get_decimator_fac(self):
        return self.decimator_fac

    def set_decimator_fac(self, decimator_fac):
        self.decimator_fac = decimator_fac

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)

    def get_WL(self):
        return self.WL

    def set_WL(self, WL):
        self.WL = WL

    def get_R_max(self):
        return self.R_max

    def set_R_max(self, R_max):
        self.R_max = R_max


def argument_parser():
    description = 'Client to receive processed radar data, providing live graphical feedback and recording of a datafile for offline processing'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    return parser


def main(top_block_cls=Radar_Data_Client, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
