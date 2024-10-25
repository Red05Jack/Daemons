#pragma once

#include <chrono>
#include <thread>


// TODO Placeholder
class NoIpDDNS{
public:
	NoIpDDNS();
	~NoIpDDNS();


	// Public Member Methods
	void Start();
	void Stop();


private:
	// Private Member Variables
	std::thread* m_thread;


	// Private Member Methods


};
