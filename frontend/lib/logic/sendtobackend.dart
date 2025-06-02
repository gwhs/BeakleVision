import 'dart:convert';
import 'package:frontend/config.dart';
import 'package:http/http.dart' as http;

class Sendtobackend {

static Future<void> sendtoback(Map<String, dynamic> data) async {
	final dat = jsonEncode(data);

	var ip = config.getip();
	final resp = await http.post(

	Uri.parse("$ip/match"),
	headers: {'Content-Type': 'application/json'},	
	body: dat
	);
}

}
