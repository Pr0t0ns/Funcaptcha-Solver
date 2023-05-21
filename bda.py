import base64
import json
import random
import time
import secrets
# import codecs

import numpy as np
from browser import encrypt as cipher


def cfp_hash(string_in: str) -> int:
    int1 = np.int32(0)
    for int2 in range(len(string_in)):
        int3 = np.int32(ord(string_in[int2]))
        int1 = np.int32((int1 << 5) - int1 + int3)
        int1 = np.bitwise_and(int1, np.int32(-1))
    return int1.item()


def get_bda(user_agent: str) -> str:
    ts = time.time()
    timeframe = int(ts - ts % 21600)
    key = user_agent + str(timeframe)
    test = str(random.uniform(124.0, 125.0))
    # print(test)
    current_time = int(time.time())
    encoded = base64.b64encode(str(current_time).encode()).decode()
    # print(encoded)
    the_data = [
        {"key": "api_type", "value": "js"},
        {"key": "p", "value": 1},
        {"key": "f", "value": secrets.token_hex(16)},
        {"key": "n", "value": encoded},
        {
            "key": "wh",
            "value": f"{secrets.token_hex(16)}|{secrets.token_hex(16)}",
        },
        {
            "key": "enhanced_fp",
            "value": [
                {
                    "key": "webgl_extensions",
                    "value": "ANGLE_instanced_arrays;EXT_blend_minmax;EXT_color_buffer_half_float;EXT_float_blend;EXT_frag_depth;EXT_shader_texture_lod;EXT_texture_compression_bptc;EXT_texture_compression_rgtc;EXT_texture_filter_anisotropic;EXT_sRGB;OES_element_index_uint;OES_fbo_render_mipmap;OES_standard_derivatives;OES_texture_float;OES_texture_float_linear;OES_texture_half_float;OES_texture_half_float_linear;OES_vertex_array_object;WEBGL_color_buffer_float;WEBGL_compressed_texture_astc;WEBGL_compressed_texture_etc;WEBGL_compressed_texture_etc1;WEBGL_compressed_texture_s3tc;WEBGL_compressed_texture_s3tc_srgb;WEBGL_debug_renderer_info;WEBGL_depth_texture;WEBGL_draw_buffers;WEBGL_lose_context;WEBGL_multi_draw",
                },
                {
                    "key": "webgl_extensions_hash",
                    "value": secrets.token_hex(16),
                },
                {"key": "webgl_renderer", "value": "WebKit WebGL"},
                {"key": "webgl_vendor", "value": "WebKit"},
                {
                    "key": "webgl_version",
                    "value": "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
                },
                {
                    "key": "webgl_shading_language_version",
                    "value": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
                },
                {"key": "webgl_aliased_line_width_range", "value": "[1, 1]"},
                {
                    "key": "webgl_aliased_point_size_range",
                    "value": "[1, 1023]",
                },
                {"key": "webgl_antialiasing", "value": "yes"},
                {"key": "webgl_bits", "value": "8,8,24,8,8,0"},
                {
                    "key": "webgl_max_params",
                    "value": "16,64,16384,4096,8192,32,8192,31,16,32,4096",
                },
                {"key": "webgl_max_viewport_dims", "value": "[8192, 8192]"},
                {
                    "key": "webgl_unmasked_vendor",
                    "value": "Google Inc. (Google)",
                },
                {
                    "key": "webgl_unmasked_renderer",
                    "value": "ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (Subzero) (0x0000C0DE)), SwiftShader driver)",
                },
                {
                    "key": "webgl_vsf_params",
                    "value": "23,127,127,10,15,15,10,15,15",
                },
                {
                    "key": "webgl_vsi_params",
                    "value": "0,31,30,0,15,14,0,15,14",
                },
                {
                    "key": "webgl_fsf_params",
                    "value": "23,127,127,10,15,15,10,15,15",
                },
                {
                    "key": "webgl_fsi_params",
                    "value": "0,31,30,0,15,14,0,15,14",
                },
                {"key": "webgl_hash_webgl", "value": secrets.token_hex(16)},
                {
                    "key": "user_agent_data_brands",
                    "value": "Chromium,Not A(Brand,Google Chrome",
                },
                {"key": "user_agent_data_mobile", "value": "true"},
                {"key": "navigator_connection_downlink", "value": 10},
                {"key": "navigator_connection_downlink_max", "value": "null"},
                {"key": "network_info_rtt", "value": 100},
                {"key": "network_info_save_data", "value": "false"},
                {"key": "network_info_rtt_type", "value": "null"},
                {"key": "screen_pixel_depth", "value": 24},
                {"key": "navigator_device_memory", "value": 8},
                {"key": "navigator_languages", "value": "en-US"},
                {"key": "window_inner_width", "value": 1365},
                {"key": "window_inner_height", "value": 937},
                {"key": "window_outer_width", "value": 1920},
                {"key": "window_outer_height", "value": 1040},
                {"key": "browser_detection_firefox", "value": "false"},
                {"key": "browser_detection_brave", "value": "false"},
                {
                    "key": "audio_codecs",
                    "value": '{"ogg":"probably","mp3":"probably","wav":"probably","m4a":"maybe","aac":"probably"}',
                },
                {
                    "key": "video_codecs",
                    "value": '{"ogg":"probably","h264":"probably","webm":"probably","mpeg4v":"","mpeg4a":"","theora":""}',
                },
                {"key": "media_query_dark_mode", "value": "true"},
                {"key": "headless_browser_phantom", "value": "false"},
                {"key": "headless_browser_selenium", "value": "false"},
                {"key": "headless_browser_nightmare_js", "value": "false"},
                {"key": "document__referrer", "value": "null"},
                {"key": "window__ancestor_origins", "value": []},
                {"key": "window__tree_index", "value": []},
                {"key": "window__tree_structure", "value": "[]"},
                {"key": "client_config__surl", "value": "null"},
                {"key": "client_config__language", "value": "en"},
                {"key": "navigator_battery_charging", "value": "true"},
                {"key": "audio_fingerprint", "value": test},
            ],
        },
        {
            "key": "fe",
            "value": [
                "DNT:unknown",
                "L:en-US",
                "D:24",
                "PR:1",
                "S:1920,1080",
                "AS:1920,1040",
                "TO:-120",
                "SS:true",
                "LS:true",
                "IDB:true",
                "B:false",
                "ODB:true",
                "CPUC:unknown",
                "PK:Win32",
                f"CFP:{cfp_hash(secrets.token_urlsafe(64))}",
                "FR:false",
                "FOS:false",
                "FB:false",
                "JSF:Arial,Arial Black,Arial Narrow,Calibri,Cambria,Cambria Math,Comic Sans MS,Consolas,Courier,Courier New,Georgia,Helvetica,Impact,Lucida Console,Lucida Sans Unicode,Microsoft Sans Serif,MS Gothic,MS PGothic,MS Sans Serif,MS Serif,Palatino Linotype,Segoe Print,Segoe Script,Segoe UI,Segoe UI Light,Segoe UI Semibold,Segoe UI Symbol,Tahoma,Times,Times New Roman,Trebuchet MS,Verdana,Wingdings",
                "P:Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,PDF Viewer,WebKit built-in PDF",
                "T:0,false,false",
                "H:4",
                "SWF:false",
            ],
        },
        {"key": "ife_hash", "value": secrets.token_hex(16)},
        {"key": "cs", "value": 1},
        {
            "key": "jsbd",
            "value": '{"HL":3,"NCE":true,"DT":"Roblox","NWD":"false","DA":null,"DR":null,"DMT":1,"DO":null,"DOT":1}',
        },
    ]
    data = cipher(json.dumps(the_data, separators=(',', ':')), key)
    return base64.b64encode(data.encode("utf-8")).decode("utf-8")
