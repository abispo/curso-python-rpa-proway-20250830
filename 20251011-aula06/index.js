import QRCode from 'qrcode'
import makeWASocket, { DisconnectReason, useMultiFileAuthState } from "baileys";

const start = async() => {
    const { state, saveCreds } = await useMultiFileAuthState('sessions')
    const sock = makeWASocket({ auth: state, })

    sock.ev.on('connection.update', async (update) => {
        const {connection, lastDisconnect, qr } = update
        // on a qr event, the connection and lastDisconnect fields will be empty
      
        // In prod, send this string to your frontend then generate the QR there
        if (qr) {
          // as an example, this prints the qr code to the terminal
          console.log(await QRCode.toString(qr, {type:'terminal', small: true}))
        }

        if (connection === 'open') {
            console.log("Whatsapp conectado!")
        }

        if (connection === 'close') {
            const reason = lastDisconnect?.error?.output?.statusCode
            
            if (reason != DisconnectReason.loggedOut) {
                console.log('Reconectando...')
                start()
            } else {
                console.log("Desconectado manualmente.")
            }
        }
      })

      sock.ev.on('messages.upsert', async (m) => {
        if (m.type === 'notify') {
            const msg = m.messages[0]
            
            if (!msg.key.fromMe && !msg.key.remoteJid.includes('@g.us')) {
                const phone = msg.key.remoteJid
                const textMessage = msg.key.conversation

                console.log('Mensagem recebida: "' + textMessage + '"')

                await sock.sendPresenceUpdate('recording', phone)
                await new Promise(r => setTimeout(r, 3000))

                await sock.sendMessage(phone, { text: "Mensagem recebida de '" + phone + "'."})
            }

        }
      })

      sock.ev.on('creds.update', saveCreds)
}

start().catch(console.error)