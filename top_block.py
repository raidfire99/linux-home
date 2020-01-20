#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Nov 24 17:19:33 2019
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, Pi=3.14159, chirp_time=260000000):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Parameters
        ##################################################
        self.Pi = Pi
        self.chirp_time = chirp_time

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2032920
        self.q = q = 10000
        self.lo = lo = 2033000000
        self.f_dev = f_dev = 10
        self.f_c = f_c = 2
        self.del1 = del1 = 524880
        self.deci = deci = 220

        ##################################################
        # Blocks
        ##################################################
        self._lo_range = Range(10000000, 6000000000, 100000, 2033000000, 200)
        self._lo_win = RangeWidget(self._lo_range, self.set_lo, 'lo freq', "counter_slider", float)
        self.top_layout.addWidget(self._lo_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=deci,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self._q_range = Range(10000, 10000000, 1, 10000, 200)
        self._q_win = RangeWidget(self._q_range, self.set_q, 'Q', "counter_slider", int)
        self.top_layout.addWidget(self._q_win)
        self.pluto_source_0 = iio.pluto_source('ip:pluto.local', lo, samp_rate, 1 - 1, 1000000, 0x8000, False, False, True, "manual", 60, '', True)
        self.pluto_sink_0 = iio.pluto_sink('ip:pluto.local', lo, samp_rate, 1 - 1, 1000000, 0x8000, False, 0, '', True)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, 628318, 1)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_float*1, del1)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*1, del1)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_head_1 = blocks.head(gr.sizeof_gr_complex*1, 20000000)
        self.blocks_head_0 = blocks.head(gr.sizeof_float*1, 20000000)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, '/home/raidfire/gpr/data/test_multi.bin', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/home/raidfire/gpr/data/test_saw.bin', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, 3.84615, f_dev, f_c)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_head_1, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blocks_head_1, 0), (self.pluto_sink_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_head_1, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.pluto_source_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.pluto_source_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Pi(self):
        return self.Pi

    def set_Pi(self, Pi):
        self.Pi = Pi

    def get_chirp_time(self):
        return self.chirp_time

    def set_chirp_time(self, chirp_time):
        self.chirp_time = chirp_time

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.pluto_source_0.set_params(self.lo, self.samp_rate, 1000000, False, False, True, "manual", 60, '', True)
        self.pluto_sink_0.set_params(self.lo, self.samp_rate, 1000000, 0, '', True)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_q(self):
        return self.q

    def set_q(self, q):
        self.q = q

    def get_lo(self):
        return self.lo

    def set_lo(self, lo):
        self.lo = lo
        self.pluto_source_0.set_params(self.lo, self.samp_rate, 1000000, False, False, True, "manual", 60, '', True)
        self.pluto_sink_0.set_params(self.lo, self.samp_rate, 1000000, 0, '', True)

    def get_f_dev(self):
        return self.f_dev

    def set_f_dev(self, f_dev):
        self.f_dev = f_dev
        self.analog_sig_source_x_0.set_amplitude(self.f_dev)

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c
        self.analog_sig_source_x_0.set_offset(self.f_c)

    def get_del1(self):
        return self.del1

    def set_del1(self, del1):
        self.del1 = del1

    def get_deci(self):
        return self.deci

    def set_deci(self, deci):
        self.deci = deci


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=top_block, options=None):
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
