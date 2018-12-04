import sys
import web3
import xbr

from accounts import addr_owner, addr_alice_market, addr_alice_market_maker1, addr_bob_market, addr_bob_market_maker1, \
    addr_charlie_provider, addr_charlie_provider_delegate1, addr_donald_provider, addr_donald_provider_delegate1, \
    addr_edith_consumer, addr_edith_consumer_delegate1, addr_frank_consumer, addr_frank_consumer_delegate1


def main(accounts):
    for acct in [addr_alice_market, addr_bob_market, addr_charlie_provider, addr_donald_provider, addr_edith_consumer, addr_frank_consumer]:
        level = xbr.xbrNetwork.functions.getMemberLevel(acct).call()
        if not level:
            eula = 'QmU7Gizbre17x6V2VR1Q2GJEjz6m8S1bXmBtVxS2vmvb81'
            profile = ''

            xbr.xbrNetwork.functions.register(eula, profile).transact({'from': acct, 'gas': 200000})
            print('new member {} registered'.format(acct))
        else:
            print('{} is already a member (Level {})'.format(acct, level))

        eula = xbr.xbrNetwork.functions.getMemberEula(acct).call()
        profile = xbr.xbrNetwork.functions.getMemberProfile(acct).call()
        print('EULA: {}, Profile: {}'.format(eula, profile))


if __name__ == '__main__':
    print('using web3.py v{}'.format(web3.__version__))

    # using automatic provider detection:
    from web3.auto import w3

    # check we are connected, and check network ID
    if not w3.isConnected():
        print('could not connect to Web3/Ethereum')
        sys.exit(1)
    else:
        print('connected to network {}'.format(w3.version.network))

    # set new provider on XBR library
    xbr.setProvider(w3)

    # now enter main ..
    main(w3.eth.accounts)
