#pragma once

#include <string>
#include <chrono>
#include <thread>


// TODO Placeholder
class NoIpDDNS{
public:
	NoIpDDNS(const std::string& configFilePath);
	~NoIpDDNS();


	// Public Member Methods
	void Start();
	void Stop();


private:
	// Private Member Variables
	std::string m_username;
	std::string m_password;
	std::string m_hostname;

	std::thread* m_thread;


	// Private Member Methods
	bool UpdateDDNS();
	std::string Base64Encode(const std::string& input);


};
