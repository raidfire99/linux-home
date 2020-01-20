#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Simulator Fsk
# Generated: Tue Jan  7 12:24:42 2020
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

from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import radar
import sys
from gnuradio import qtgui


class simulator_fsk(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Simulator Fsk")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Simulator Fsk")
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

        self.settings = Qt.QSettings("GNU Radio", "simulator_fsk")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1500000
        self.blocks_per_tag = blocks_per_tag = 2**17
        self.samp_per_freq = samp_per_freq = 1
        self.freq_res = freq_res = samp_rate/2/blocks_per_tag
        self.delta_freq = delta_freq = samp_rate/4
        self.center_freq = center_freq = 1000000000
        self.velocity = velocity = 20
        self.value_range = value_range = 10
        self.v_res = v_res = freq_res*3e8/2/center_freq
        self.threshold = threshold = -120
        self.samp_discard = samp_discard = 0
        self.range_value = range_value = 10
        self.range_time = range_time = 10
        self.q = q = 1000000
        self.protect = protect = 0
        self.min_output_buffer = min_output_buffer = 2*(blocks_per_tag*samp_per_freq*2)
        self.lo = lo = 2033000000
        self.gain = gain = 70
        self.fft_size = fft_size = 512
        self.delaytime = delaytime = 0
        self.decimator_fac = decimator_fac = 2**7
        self.R_max = R_max = 3e8/2/delta_freq

        ##################################################
        # Blocks
        ##################################################
        self._protect_range = Range(0, 100, 1, 0, 200)
        self._protect_win = RangeWidget(self._protect_range, self.set_protect, "protect", "counter_slider", int)
        self.top_layout.addWidget(self._protect_win)
        self._gain_range = Range(0, 70, 1, 70, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "gain", "counter_slider", int)
        self.top_layout.addWidget(self._gain_win)
        self._velocity_range = Range(-30, 30, 1, 20, 200)
        self._velocity_win = RangeWidget(self._velocity_range, self.set_velocity, "velocity", "counter_slider", float)
        self.top_layout.addWidget(self._velocity_win)
        self._value_range_range = Range(0, R_max+R_max/2, 1, 10, 200)
        self._value_range_win = RangeWidget(self._value_range_range, self.set_value_range, 'range', "counter_slider", float)
        self.top_layout.addWidget(self._value_range_win)
        self._threshold_range = Range(-200, 1000, 1, -120, 200)
        self._threshold_win = RangeWidget(self._threshold_range, self.set_threshold, 'Threshold Peak detector', "counter_slider", float)
        self.top_layout.addWidget(self._threshold_win)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimator_fac,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimator_fac,
                taps=None,
                fractional_bw=None,
        )
        self._range_value_range = Range(0, 120, 1, 10, 200)
        self._range_value_win = RangeWidget(self._range_value_range, self.set_range_value, 'range', "counter_slider", float)
        self.top_layout.addWidget(self._range_value_win)
        self.radar_ts_fft_cc_0_0 = radar.ts_fft_cc(blocks_per_tag/decimator_fac,  "packet_len")
        self.radar_ts_fft_cc_0 = radar.ts_fft_cc(blocks_per_tag/decimator_fac,  "packet_len")
        self.radar_split_fsk_cc_0 = radar.split_fsk_cc(samp_per_freq, samp_discard, "packet_len")
        (self.radar_split_fsk_cc_0).set_min_output_buffer(524288)
        self.radar_signal_generator_fsk_c_0 = radar.signal_generator_fsk_c(samp_rate, samp_per_freq, blocks_per_tag, -delta_freq/2, delta_freq/2, 10, "packet_len")
        (self.radar_signal_generator_fsk_c_0).set_min_output_buffer(524288)
        self.radar_qtgui_time_plot_0_0 = radar.qtgui_time_plot(100, 'range', (0,2000), 10, '')
        self.radar_qtgui_time_plot_0 = radar.qtgui_time_plot(1, 'velocity', (-10,10), 100, '')
        self.radar_qtgui_scatter_plot_0 = radar.qtgui_scatter_plot(500, 'range', 'velocity', (-10,2000), (-40,40), '')
        self.radar_os_cfar_c_0 = radar.os_cfar_c(samp_rate/2/decimator_fac, 15, protect, 0.9, 30, True, "packet_len")
        (self.radar_os_cfar_c_0).set_min_output_buffer(524288)
        self.radar_estimator_fsk_0 = radar.estimator_fsk(center_freq, delta_freq, True)
        self.pluto_source_0 = iio.pluto_source('ip:192.168.3.1', lo, samp_rate, 1 - 1, q, 0x8000, False, False, True, "manual", gain, '', True)
        self.pluto_sink_0 = iio.pluto_sink('ip:192.168.3.1', lo, samp_rate, 1 - 1, q, 0x8000, False, 0, '', True)
        self.low_pass_filter_0 = filter.fir_filter_ccf(6096, firdes.low_pass(
        	1, samp_rate, 1e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self._delaytime_range = Range(0, 50, 1, 0, 200)
        self._delaytime_win = RangeWidget(self._delaytime_range, self.set_delaytime, "delaytime", "counter_slider", int)
        self.top_layout.addWidget(self._delaytime_win)
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, 'localhost', 3333, 1472, True)
        self.blocks_tagged_stream_multiply_length_0_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, "packet_len", 1.0/decimator_fac)
        (self.blocks_tagged_stream_multiply_length_0_0).set_min_output_buffer(524288)
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, "packet_len", 1.0/decimator_fac)
        (self.blocks_tagged_stream_multiply_length_0).set_min_output_buffer(524288)
        self.blocks_multiply_conjugate_cc_1 = blocks.multiply_conjugate_cc(1)
        (self.blocks_multiply_conjugate_cc_1).set_min_output_buffer(524288)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        (self.blocks_multiply_conjugate_cc_0).set_min_output_buffer(524288)
        self.analog_agc_xx_0_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0_0.set_max_gain(65536)
        self.analog_agc_xx_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.radar_estimator_fsk_0, 'Msg out'), (self.radar_qtgui_scatter_plot_0, 'Msg in'))
        self.msg_connect((self.radar_estimator_fsk_0, 'Msg out'), (self.radar_qtgui_time_plot_0, 'Msg in'))
        self.msg_connect((self.radar_estimator_fsk_0, 'Msg out'), (self.radar_qtgui_time_plot_0_0, 'Msg in'))
        self.msg_connect((self.radar_os_cfar_c_0, 'Msg out'), (self.radar_estimator_fsk_0, 'Msg in'))
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_multiply_conjugate_cc_1, 0))
        self.connect((self.analog_agc_xx_0_0, 0), (self.blocks_multiply_conjugate_cc_1, 1))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.radar_os_cfar_c_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_1, 0), (self.radar_split_fsk_cc_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.radar_ts_fft_cc_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0_0, 0), (self.radar_ts_fft_cc_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_udp_sink_0_0, 0))
        self.connect((self.pluto_source_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.radar_signal_generator_fsk_c_0, 0), (self.analog_agc_xx_0_0, 0))
        self.connect((self.radar_signal_generator_fsk_c_0, 0), (self.pluto_sink_0, 0))
        self.connect((self.radar_split_fsk_cc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.radar_split_fsk_cc_0, 1), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.radar_ts_fft_cc_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.radar_ts_fft_cc_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_tagged_stream_multiply_length_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "simulator_fsk")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_delta_freq(self.samp_rate/4)
        self.pluto_source_0.set_params(self.lo, self.samp_rate, self.q, False, False, True, "manual", self.gain, '', True)
        self.pluto_sink_0.set_params(self.lo, self.samp_rate, self.q, 0, '', True)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.set_freq_res(self.samp_rate/2/self.blocks_per_tag)

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

    def get_velocity(self):
        return self.velocity

    def set_velocity(self, velocity):
        self.velocity = velocity

    def get_value_range(self):
        return self.value_range

    def set_value_range(self, value_range):
        self.value_range = value_range

    def get_v_res(self):
        return self.v_res

    def set_v_res(self, v_res):
        self.v_res = v_res

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_samp_discard(self):
        return self.samp_discard

    def set_samp_discard(self, samp_discard):
        self.samp_discard = samp_discard

    def get_range_value(self):
        return self.range_value

    def set_range_value(self, range_value):
        self.range_value = range_value

    def get_range_time(self):
        return self.range_time

    def set_range_time(self, range_time):
        self.range_time = range_time

    def get_q(self):
        return self.q

    def set_q(self, q):
        self.q = q
        self.pluto_source_0.set_params(self.lo, self.samp_rate, self.q, False, False, True, "manual", self.gain, '', True)
        self.pluto_sink_0.set_params(self.lo, self.samp_rate, self.q, 0, '', True)

    def get_protect(self):
        return self.protect

    def set_protect(self, protect):
        self.protect = protect
        self.radar_os_cfar_c_0.set_samp_protect(self.protect)

    def get_min_output_buffer(self):
        return self.min_output_buffer

    def set_min_output_buffer(self, min_output_buffer):
        self.min_output_buffer = min_output_buffer

    def get_lo(self):
        return self.lo

    def set_lo(self, lo):
        self.lo = lo
        self.pluto_source_0.set_params(self.lo, self.samp_rate, self.q, False, False, True, "manual", self.gain, '', True)
        self.pluto_sink_0.set_params(self.lo, self.samp_rate, self.q, 0, '', True)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.pluto_source_0.set_params(self.lo, self.samp_rate, self.q, False, False, True, "manual", self.gain, '', True)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_delaytime(self):
        return self.delaytime

    def set_delaytime(self, delaytime):
        self.delaytime = delaytime

    def get_decimator_fac(self):
        return self.decimator_fac

    def set_decimator_fac(self, decimator_fac):
        self.decimator_fac = decimator_fac
        self.blocks_tagged_stream_multiply_length_0_0.set_scalar(1.0/self.decimator_fac)
        self.blocks_tagged_stream_multiply_length_0.set_scalar(1.0/self.decimator_fac)

    def get_R_max(self):
        return self.R_max

    def set_R_max(self, R_max):
        self.R_max = R_max


def main(top_block_cls=simulator_fsk, options=None):

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
