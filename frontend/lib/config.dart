

import 'package:flutter/foundation.dart';

class config {
	static String BACKEND_IP_TESTING = "localhost"; // for testing stuff
	static String BACKEND_IP_PUBLIC = "5507.org"; // this is the one we will use in the built version(s) of the app

static String getip() {
if (kDebugMode) {
return BACKEND_IP_TESTING;
}
return BACKEND_IP_PUBLIC;
}

}
