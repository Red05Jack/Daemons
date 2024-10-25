#include <iostream>

#include "NoIpDDNS.h"


// Main
int main() {
	NoIpDDNS ddns = NoIpDDNS(".\\config.json");
	ddns.Start();
}
