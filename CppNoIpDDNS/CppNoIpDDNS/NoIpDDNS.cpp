#include "NoIpDDNS.h"

#include <fstream>

#include <nlohmann/json.hpp>


using json = nlohmann::json;


NoIpDDNS::NoIpDDNS(const std::string& configFilePath) : m_thread(nullptr) {
  std::ifstream configfile(configFilePath);
  if (!configfile.is_open()) {
    exit(1);
  }

  json configs;
  configfile >> configs;
  configfile.close();

  m_username = configs["noip"]["username"];
  m_password = configs["noip"]["password"];
  m_hostname = configs["noip"]["hostname"];
}


NoIpDDNS::~NoIpDDNS() {
	Stop();
}


// TODO Placeholder
void NoIpDDNS::Start() {

}


// TODO Placeholder
void NoIpDDNS::Stop() {

}


// TODO Placeholder
bool NoIpDDNS::UpdateDDNS() {
  return false;
}


// TODO Placeholder
std::string NoIpDDNS::Base64Encode(const std::string& input) {
  return "";
}
