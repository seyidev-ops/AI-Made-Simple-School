/**
 * AI Made Simple School: one Google Apps Script for
 *   1. newsletter signups ("Stay ahead of AI") + welcome email
 *   2. one-click unsubscribe
 *   3. the weekly AI brief email (sent from updates@ your domain)
 *   4. first-use access codes: starts a code's 30 days the first time it is used, and stops sharing
 *
 * GENERATED FILE: google-apps-script-ams.js is built from tools/codes/apps-script-template.js by
 * tools/codes/generate.py (it injects the list of valid code hashes). Edit the template, not the output.
 *
 * ── SET-UP (about 10 minutes, once) ───────────────────────────────────────────────
 *  1. Sign in to the Google account that should SEND the emails, open https://script.google.com
 *  2. New project → delete the starter code → paste this WHOLE file → Save (name it "AMS Mailer").
 *  3. Project Settings (gear icon) → Time zone → "(GMT+01:00) Lagos". Save.
 *  4. Run → setupSheets   (approve the permissions the first time: Sheets, Gmail, external requests).
 *  5. Run → installTriggers   (sends the weekly brief automatically every morning a new one exists).
 *  6. Deploy → New deployment → type "Web app" → Execute as: Me → Who has access: Anyone → Deploy.
 *     Copy the Web app URL (it ends with /exec).
 *  7. Put that URL into ams-config.js on the website (apiUrl) and publish the site.
 *  8. Run → testWelcome (type your own email in the function first) to check the email arrives.
 *
 * ── SENDING FROM updates@yourdomain ───────────────────────────────────────────────
 *  Gmail → Settings → Accounts → "Send mail as" → Add another email address → updates@yourdomain.
 *  Gmail emails a confirmation to that address; you must be able to read that mailbox (forward it
 *  to your Gmail or use Google Workspace). Until that is done, emails go out from the Gmail address
 *  that owns this script (the script falls back automatically; nothing breaks).
 *  Also add SPF, DKIM and DMARC records for the domain so mail does not land in spam.
 *
 * ── LIMITS ────────────────────────────────────────────────────────────────────────
 *  Free Gmail: about 100 emails a day through a script. Google Workspace: about 1,500 a day.
 *  Over ~80 subscribers on free Gmail, the digest continues the next morning automatically.
 *  Past a few hundred subscribers, move the list to Brevo or MailerLite (free tiers) instead.
 */

var CFG = {
  SHEET_ID:   '157udafPnTILbRYp9TbgD6FQgPOTuCo5iL4jeDg4Suwg',
  SITE:       'https://aimadesimpleschool.com',
  FROM_EMAIL: 'updates@aimadesimpleschool.com',
  FROM_NAME:  'AI Made Simple School',
  REPLY_TO:   'updates@aimadesimpleschool.com',
  POSTAL:     'Ona Services Limited, Abuja, Nigeria',
  BRIEF_CAT:  'Weekly AI Brief',
  CODE_DAYS:  30,
  MAX_DEVICES: 3
};

/** Hashes of every valid first-use access code (injected by generate.py). */
var VALID_HASHES = ["f8b5f30d3887ac2cc9b1d4c9567a1cb0150e866b7b182bbfa7ebd9691cefd61d", "350fc0ebae2d0122fedb2ff54b7c82712e24bac03c6494a84da2430be6fd8dbe", "707d663fa424f743d29bef20d4e3ca6fa91f8bbfef2810f89ca62510ef3fb590", "99b80a46ec68a592925fb575be86f09660f37c5b6f9d74b0649694a5631011f4", "6db188ec85bbd85586ac438eed4ae8a1e84f3942ccfe1e0b43e0e6bbfcacc4df", "7cef1b45c5c6b3a4cbab99a74d20893da20d691096b8cbbcecde016bc5b9ec87", "68a34de15bb039bc10f3b2731635bd8468e78c149dc20bd30cc6b89743636892", "aecb6de266cc1abcfca32f6b0ae24619f721366d8ba80fbd07c0b3bf7c200421", "0f802baa6a81cef1c2e91faebfc9f4a005de4469dba6f36c41993450cf79baac", "bb2d4c001f78f307b7824a7699ddcdd9f1fc934063d230ab0de11e61094655d9", "f79cf83acb1aeeda1d0a547628ebeab8f5396ff35b6c51729d95f8e9510160bc", "c109345f5e19a8bdd91a5025f0a57fc3fd39a7af67712428cfd5ff8267fe4d9b", "45ced943b15908bd5af0f653849d4a01c7a23301562f595caa37dcc2bdf49bf3", "1e772c996b56c78df67abcc0b8e15e1613116fa05531c4a05bf730d4f49cdc96", "d4a67bcd23ae3d5ac988d01d4bef04b60ff1a369d58da7b418648bfcd1340df6", "8da6bc4fa5c99ad9f45706abc8fb034293c5d1433d7046598945ae558a5bd40e", "b3bcd9720d28bc87862f04b129908d058cbe895a067cc13c1bc971a8d102ffd3", "59c0c46d9535b81f7194d3ffb94c7bc87472d31ff0333a586cfdb964d3381092", "df8655d061e5bd00e47847ac50fbc9eb75443710696f3ba41d330fe35c973a0b", "e1384ff8e9e327424c80e7fd13fa9eed664ee96880192361d5f6d2ef388636a1", "9fc0716aa72522f28e24f69773e0c36246fe6d0a7bf5fe338d60e49552c7b93d", "82d7ad1f6fb9ea397a6ff4122b9256e1b3b18719ca77cfbe906fd0d910e7e3e3", "5bfc4050078e20b2afcfe2cd25652cc808d7539f0c18466e0c0c5f0b9f174b5c", "eadaee3f2aabfeb695e55cb6a53f1a41987470511553947563fe0c7db4498d94", "931d47f4bd21a76a4b9365eb39b4be24eba00c450567a00727d356d30c3cc7f1", "f82390c8eab1253e53ab50acce3879890a70b3a653547f19159cea19476b097e", "e3f03a809136e7bec5237da02830cfcc55181f3dfe21cdab76c6d7b05065c4f6", "b9cfa83207f540a7d588fe0ddcf11bde99f22dac65bfeefbcff97e7de26e7a1d", "f3356257c22fa0c4e82f52e9a61d0e74b7f80364fad75a59830edc80ce119331", "a655dc64add3a71d27da033ffbb069d5c6f5473bb2aa5b34e779a235370554fd", "a3f33340cc30449c43e931ae79f12be5216bc4d7a025dd46a38b20b07e8f8a8a", "f26226e07f5ee1a54f47ccb7e8c7974798e8899c986ae0c3511fd09660858a07", "9c69bc7d10c1becfa6b92ff01593199acb5c43ca2ae3a84093fb9891ba9a6a6c", "257866b70dc08c7603cd5f7c866f62e38d7e39493875fe20131293b703eaaf28", "e0e4264763fc80caa5943868a7a7b6d72746836accf8768b55493350d845bdec", "058780964e45106d5d7a33c40a1fde8940124b8dd4b86d66c13aa4ddc2a85cb4", "d7daea5d8e2f11f5dcd718397f68a5e3cda333f3342cc9a79bae6f2acd4f1fbe", "a535e4c4088a3a6ac525a05f17f5b7ab9f72f360739bd41ba846af5434dc81a6", "af48414b81d3d90837afc4a35ad8a99b1e7b7e8eb82cdb25eab367f4581e2743", "cab65db4f4705b89907a529d57c2bc897a58ee778c0bd5b68e8d13e6cd54dc8a", "261f0619127c7c61b3078c333bbf58065f8e1e2d1ba73d1415a2d0af2da45807", "172d924299aa78d69879983696b27111faf7e270e36c4ee9d942ddc9525e2274", "7d038448db8650e2180a0d3b17ac0066ee8ec11f7addc51a89956759c590b92e", "6f83d4093698b060e952aee423220580b64ef2af3c4dbbebeccf06ae947c3d5f", "16cebc2f38c00f8681ad3b2261166569c7fa094cd5dc5220c377f8f4b4feb3d7", "641a9c04d9faaedf3ed474975cec1184aa413f3231101bd5c67a7375af9e6363", "627986db3c1522268e8bb95482b7f4e76f4ab87190a81e63137a79c80a92df0b", "4c351bdf31172747817300bf71147a5672ca7577f9095691050857058c4709da", "60f3caf1672978785af2b9f3733e3555e428d0385df3890a85ea7a2421a355dc", "f0a3766aab72e9bc74086c1140f2c76369e4351dc9ac410f55f481b68255d75c", "621a226b8f6676910d2aa2e6ceb283bc3f98c8938b04516b0a04196cdcf1ae5b", "0de716f33b8ac90d1ebb6768c08f1fe7165633d09ee37646eabac679a6a7d8aa", "48714d5d4f8ec133e66027be539996ba81f855b4a46ffc912bd0450178daa8d8", "1b638d4371f39af6fe92f0daaa2cd1f3c8690f7b320c568ff1463d374ad8aede", "9a4fa1ba7893bff9cb87aef19f03e0a6a5be5bcf714b4876631691c3742db24c", "a0bfe8405c85be99d672c6e7aaf5bb5bfcf31cc9164062bc4d536a3e38f13eae", "1b896fe2a51793c69592baa35401828e170e63237f63156b2a38b43a7cee9468", "d3deeac56ec9bb9706e62620235d2c266e695e29858100faac43fa7a00d03afc", "98cd0bc1b51b4eaec6810d6485bf6e5b7de058b2fb93a7cd7c55dab4a7d5265b", "ea25fcf6ec8210645bd684351785b5acde7ad76488004d5e35fa4016cb9c10ba", "7a69e78f4f784bc90d841e8add3d4fe9f77b8e045bd8d08971f26a994f97080f", "ab4f13d7d44ad4e17c42acb63e00098490c237cd8ed386c6e64fd1824ec20614", "508da9aa51bff96361b4953842a8d596772f6e082daea6bfe40c37feb19c0647", "a8ae89595aa66a289a52feb32f332ed2ed6e3f2078bbfc5cc4193fa62f4f3452", "c41bba5052a4ebfddaeaf737348686e22273f719afdbc717aa42b465650dce9b", "66394b454266e3083b151f59682b6f30d87c1718d94dcc9b918485329dc6e4d8", "c1609a80d813106fda4f9f0a4e65f9c7dce21027d17dd15f6daa468f145a25ef", "1cf805ef66a09363bb548a818de2e276124258933d11dabca92c013190b62f33", "e7b01252e522fc6569ecba6f59c08d8a2e7eff1da69905b78afe8ae17241bd41", "1ca1ea53132084188d0294a3f06a79c3fcf93cb7cd0af37b4db0dad02b59dc82", "f0bfc27719ca770b6b99890a781bb106fee90195da0bec3468be9c17f2d851ff", "5ffc6c498190914c65366e250481d9439583820b811ae1903e86936a2e0a9e16", "a832b4551c64386bc870552f92cf32ce22fe6945eab5c254fe7baf1aff012f47", "34ed8b6f260406ac54a26b1b0463aa1b67bbf571055e3e8d55e5b35559b22619", "d377c1c04dc4e34f7068edf6132fda2c56a69722e5db672a7261d1644cecd3f0", "66efbab9d627d73900e0d817f465146e968e2cec4d6381c0394015001f29506f", "56f0921ded0116c8b03d4e5638c0e3fb23d992d453f9ca56260b455d9b49a8d9", "6da330f27816baa6b24de58a9a7849aa0c159bda82bdb5e1f5135fa9e9d442d8", "e967c20b8b6b156c28c5e6b35606d431468edabf612d431316536891fbd8f144", "958932305625f636d1bdae5c18a1ffa9ca77103287f8095e390eb853a2de1408", "71e63af8337cc6f8baf7e17b6bfecdd293176cba85742df4d29e6a53173c4706", "aac47e9a0ee15c279e0126116988a666d6c903145d836f81cefd0059b4680ff3", "4349a4e7d2f571881b32d5f6f0c82ee9e9ed55c4bdcd2b93e61ceeb5728b43b3", "996e606914b4f399d3d68b1068751390ab62e66b196b2c0136cc837cf0fc17dc", "4a01c3023e9fd962d19a7f7ede37916df976669cf70063aa00be6de385373d5a", "4fd5b243a31664b50192c7bf6d7ae172a8452cdc979d9c67fef06f982722cc9d", "a42d30cac7a109f54d0ee42d80cfaab9c3d9acd7759d65156cb4d57a001b533b", "fe231bef50f5a8a41aa48949e58b618f1cc0e85b11a817070af2981e11ad4cd8", "80edd79fcb392273ae2c56ad6935ca2021b250c7ccb7c91f42c5561f866fe61a", "8cb4389b79806f91209be89cea7aab72bf2a3f42a384ce38bbb71ba1f8c017e8", "4ba752efa90ea6426b1adeb84faf13baf197921216856d9869faaa9fc0abb843", "0be4a717f3dd102c9300113be05f5910a9b3b7802c1c5ae7cd83d1c78d43d123", "4092bc5d3afb636760a1c695a046a5c0acc5b9d97b4b86b7fee15d52d6556ffb", "2138bac8fc67a408ffea7bff09b6ce8b44c508ff761f7f0be206eb898b102cf6", "325f6db2ea6039bb5babec7d36d9211e7e520632c779de51185060f14e328381", "f91c0c67d877da9bf050ebcc4cb8bf3a761d4b937019a54330a40c05e11cba07", "672f576a7e294d7f11ea205e07c20da79ab97d2e9e4deb8cf0a5407a43c3362a", "ad29b05bb98ec143c556cee4a4b58f38e1921e1fbe2d8e98e80362a4ebbe487f", "3482f899414774899e82638e9e413d0560d556b88868a6dc3ad762f443a1e1f1", "16c37fc6d2e06efe74e54f50187b4b9cf06fdf3e671f131a4fac16f920838959", "70a74ac3ed0cdd615ee25161c779277b8fc92e449ad35cb5b297dc2f0bd24e0e", "3b83e4a632583ba4c92a96c85cb7ffb27ca69194debad2d7d11702440d7bf822", "4d212b99d3f5f03f6989a7cd60ebec3445388bdd915c7545ad84aa97942a6993", "7f021534d58cdd999a047ffa1c41e76fb5eb0e5d1bad2ea23422df2aaa5bdfab", "603e892b7922be187768dd932d129e82bf64306ca5bf678eb7caa58aa9b61347", "85f7f2a84969bd2349c4a878d2b5b3b5664357ec5a22d14f9f8bc9292c472dfb", "3b845c10fbac3441d0931b914ddf7ad62ec77584052bb7f496b55b284553c58b", "8c90834a52e3c0b1ed28e020d4ee375379966ceb3e8ee7e3f41d38726745b7ec", "e605039602229e524db72d2e71ce36433c6401baf7dfb4e8dde14d1014458351", "d606bd16d14d4d19ce15e0d00d56ebd71fba0bf6434ca6afac334b1dc84e679b", "1a2565927e8475cf560a4cb1ab6a44480d6fff86c60489d88e91f966d7645f50", "76687d706e1f257b16fe5d9cbc05ace205d975612cc5967777872bef45735dbf", "0c8283389e69b65baca6e07a19e85e60e0645b54d6fc95f83252025d0e96e373", "9d5958bfd115ee96f99c1a5a6486972cf074c1e6f842647e7846e4fe7b733dc2", "b293d16faf232f0521777310b02f5ac8aeb3b1a8160260f15516ef6147378837", "4620eb03e8da14dd5b3d081b5522b1ade06871d71b30d994a008b06e8214b134", "62a574c3a084de1cb8b84784feba633d296336d143be8d5e6f37739f8931cb71", "3272f6a71e0365da2084febc94aa10e43a449eeab20a9d4278786e20e7de001a", "0dfcb6e80c89a2cd7f3d420177d05b64b648fe6a2b52215cffa7df527080ebed", "ba5160ed508d587961770115e94c31b98aa47ed248fe2dc6c690528321c0078e", "c876eae858db5e3593c2ccdf399c53ca1cea49d5ef3c990b84f0df239b0faa64", "7f5ce2cff1689a3e7c09ffbf251819708ca3434798b2b427cc87315e5666c8ab", "5e3bf2a896c54fda8457f259343b66adc85333010c9dea23faf9a3325f12c64d", "a7c7aee6a19c2204c92abaf1574b5bcd6df5130aa6b13c9faea53512fdd2e444", "26cc601e13f785aa0510828ad0644af8b5787ac42cf7a49b3277aef098314c30", "f65e6432ad91cbd47cf393897afda6fb725518f40df4a18d80e4135fffad3d6d", "69eb445b66ab22e144741f73c64b4a9b62352c0519fb8367fdf00a405d797ca1", "884fe0dcb3bbc7d761bc23b69b26ed39fef87213cfb63ac9c1edb421c7c3bc53", "f3a41b2da59bd5422b1fcfa5e5d8e24d9e516e8af37358b4e92e4a47f77cd6ae", "e48f7c533c58c96e79336884d05a05712bc8a93315be69d398dee4e438488066", "f3f9d257673f78893af6d03684ea564d32a08a48bd88a2767db1d81b09418920", "d9f08275f01fec9d9cb4a654563506ce29da2aa43676968ce364ba3b8265cf02", "4bc1bf1d86238216de2a1259192db6a30433db2cb25958b09e3380e3e3161bb8", "873b1bad5602beae01ea93fc4a9f8fe694b7155030a305c02e0577a6e9f5cdfd", "ffa59abcd6a9dcdababe5d80523af20ce8067b4f2d40e3e104c39909b09caf5b", "dbcb772f5533eaa77dcae1a388a863a4c9e2574086d3b3ef5caf261e46a18781", "fa6d0a74af012edd08bfa73a6ecb2a50e9d54fb618d9c1cca9ff345648073edf", "35210c1bd3094b79d6e3d6b662e019be56647cdb8e618549b842f356cb5fc0b2", "6c861c91a7eaa8a38e00337aae7ad804d7d0cd194e76ef216c3a5c2e58d4adfe", "8dbdc7c4afbca74c332c35f5951438ccc07cb91dca46b6e2e082126266dad0df", "aa391e164942fb5ff83ce46dcba82ad96d5e9594207dd81772a0a620c3e92576", "12b9ab25210dd37dceffbe307f3316e05d26c5b7aa8542c12eec12d032ec8c01", "70a7eb28a3bfdfdc93a7c97c0160d5397506c9981491bfea19df141eae0466dd", "3b3627892920501d18ac3a8bb7bb1de15293b468a2eb12d1c9a6329ca6a02ab4", "7376414050e38a5d6b65b2c273a1a37a7d837efa8cd01406c0d30842f4b61753", "b319efbbbad116ed8a89d58516c24ccec2a6dd0782169d8d221cbaada2785162", "27d4aed1bf323d2b9ffb84e5bbae93347205d09c365c593c894141d899135968", "30df78bd62a6ef6356caedce55e2ac95fd7e498925eaa9a6db6334e8b214f832", "3e6e3c527064a4d7eb897feabb6cb54b1df5268eeb9618179089d46996625b53", "8b11365ef71b232012e077d44158b0cef1cc8ffea1f9216a0d396c4527a2d97d", "eb4eea80c170bbc7c313d79bcc754fb979719cccfe14a604803aebfb6a2d5936", "49793eb71bdb7ac6bc385de0da2ed49343912c3ef87e9ca0d69ab322d131baa7", "69e2da2a054780abda361a161aaddb654de9c4ec3862d4d6a3a6eca6708a6776", "60ebedf676a8270d96bb8bb245daa616f38554b4b89603d9578d7814b9d6b635", "bba6ff52c369d2186c0861dc397d010eadfe7243a600566f0e5277a0fadb65fc", "94af19b8129d365e6ce1c23f77495f7cb444e0efcaceb3805105c3209393e4e4", "981b6e69e508472ff9680ced08a513c6926e6ad3be876d29c315c678d5ba36a7", "53759d87e4bb606f50bfa5ec8a364d0b94a00a8c4271fa3743f5347c7c375746", "e3bdf8f139cba9ff3e0b0add8e9bc680f273550776f12367f1cc3e0c64f6969f", "7286b135c4e4e6662ee52a44bd1e861cca5e1571c5f9c5730904611ec1cae901", "63457777e6799cb46991c0ac91c0af11c4e6abec0984f49917365629f0aec4f6", "9ac76536b8343ab2fdcd7a38b82b7814e3d203734daf269b1f7aaca93a294df7", "b8531bc9789e8d8904ae8344fb35000de2678bc44d3afd130dcbd731d7cab685", "1eb1e4af70cfa940032a8162568e215ca840fcc5b7ee9296231bc925d8f666cc", "3594f3d61e2d811725f28dbc9035686c223eb97cbb31ec718fadf56ac3b19dd6", "fc2fa63d438ceb585ac326b39118b9d890addee49002b95c5b98b2010d4c4900", "0ba3aa9119c228ba36004052fc3d93fe765573e3e7037a87748a9db102601275", "39ad0bce357108a13db0aa049bb3ccd254f2273c66cb098f7897ed28da432f6d", "918a474d2e1d46642539c124de3d86ea4f1b4eae28596b6325b4a82541ac398b", "309e3790e58b1ec409fb9963087474f4faaffc382bd503734665aefc0dd91d0e", "4eeaa42ff76f439a26abbe96688a2cb7791ba63f37128e955ee5a5d0b621af02", "d1a07b81f8f8d9eda72c76c79d49ab933755c0c54eb32c501f674d28b2315c70", "56a6144dd9a73e481ba37b4ffe9b6ffdc53fbe112944f09f34faed3ce1eac0c9", "805772a3ebf3ff4b829fc04964870881eaa9ba735c4441fc5a6790a1d3053c21", "556f8b4c36ef479b8b5190b8e7d3b8ee3ca856950c37dd8b418bae80fe76da95", "d6bbb59a2b8085f6ae5e9c0285b4ced93c13dcd1189992f37ee3a8452d365892", "07cf679a6ed00479f9fbe60b89c462b22f0041b628b1bbce658fb59861d54304", "339e17446dffbb8b55f2e33a0250cd2cecd68ed6bba7733fd1b92aef3f2199b7", "106e2a49dbf90b4c761c4d925787ed5a70b00cf99c6792f32405cdbccf6bba1b", "5428bd9f7fa5a87a733e5ea371840573c64055c0ab744fc51c3501262272e040", "091d72ba3ceb7f5390389ec58d1c006bbb820193996583f27579cf7c0ce2753b", "588b50e774c571320d76fed8bddb12ad9d54c0a3e0e913ca0588469617f3b82f", "ddc6139e08fb0bfd2ed133d9fed3476a98d01be4db5a13bc311afa3bd00c6d81", "921185416f533405f2ed14bfb2939f95e269e8176f0bb93a6832a1782bb06d5c", "78d7d4d01f70e0ba92fae2a6f15f62bba28f6785a8af007f1369b06a44034ef2", "7f0acf63d220b01507db7d0e291927176ad161c91bfefea34c2e124856238fee", "773488a00f0994aa7a5dbd761e3151a923f204a73ad478e0793121b32423aa77", "ff3a1a24d12b3deaf74f71b6e4420499876a0fee7e4f86a27a432468fc8d1ff8", "86961a07cf5f061fd9410fa793029f2014442fa14ff68ae006aad45628601c6e", "ccfdd5ded144c2e24407a24104bd2283adb632ae9a98a34f549ddfd688b86213", "758109fce83e2ba5b853db8319bbb75dd561c4e1c93faee3dc8f12cbc2c9cdf7", "a0490f847e3db2d50d11c11ac549a263eb2d29c54bfc313bb481e00ab70066ef", "ad8eda51fc7705fb993b911c042bed57a78871354319e54ca7d05f99d92fcc87", "8ec4eef0cfa62cdf4fa0319ea482c23dcbbc5e9b2638fc688ec5bb8ba9aa269a", "41e41ccab3bcbcb20efe6fd4a9f4a83d0c6897693a2fa0e6c31c5a35805f5853", "af50e7a248539ca6bb5a9edce8edb214a2bd46571ff27641cbb256839f2860d7", "eff5fba827be6ca4dc4d94d3b7c16c37b16aba726c36f87eabffeda6cf709973", "987c871cec8a00227853ca7923fa198f366c0b63393ca15fd24fd56157de5fa7", "3427ca8d82255bb9bc71d44853724dc88e4027196224df6fd44c41d24b8f8c56", "66ba5463e40a08230fd93a43a6bdfa93504165d7603b4dad91b02be352305cf5"];

/* ───────────────────────── web app entry points ───────────────────────── */

function doGet(e) {
  var p = (e && e.parameter) || {};
  var action = String(p.action || '').toLowerCase();
  try {
    if (action === 'redeem')      return out_(redeem_(p));
    if (action === 'unsubscribe') return out_(unsubscribe_(p));
    if (action === 'ping')        return out_({ status: 'ok' });
    return out_(subscribe_(p));                      // default keeps the old blog form working
  } catch (err) {
    return out_({ status: 'error', message: String(err) });
  }
}

function doPost(e) {
  try {
    var data = JSON.parse((e.postData && e.postData.contents) || '{}');
    return doGet({ parameter: data });
  } catch (err) {
    return out_({ status: 'error', message: String(err) });
  }
}

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/* ───────────────────────────── helpers ───────────────────────────── */

function ss_() { return SpreadsheetApp.openById(CFG.SHEET_ID); }
function stamp_() { return Utilities.formatDate(new Date(), 'Africa/Lagos', 'dd/MM/yyyy HH:mm:ss'); }
function esc_(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }

function sheet_(name, header) {
  var ss = ss_(), sh = ss.getSheetByName(name);
  if (!sh) {
    // the very first tab already holds your subscribers from the old script: reuse it
    sh = (name === 'Subscribers' && ss.getSheets().length && ss.getSheets()[0].getLastRow() > 0 && !ss.getSheetByName('Subscribers'))
      ? ss.getSheets()[0].setName('Subscribers') : ss.insertSheet(name);
  }
  if (sh.getLastRow() === 0) {
    sh.appendRow(header);
    sh.getRange(1, 1, 1, header.length).setBackground('#C9A84C').setFontColor('#0E0E10').setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}
function subSheet_() { return sheet_('Subscribers', ['Timestamp (WAT)', 'Email Address', 'Source', 'Status', 'Track', 'Unsubscribed at']); }
function redSheet_() { return sheet_('Redemptions', ['Code No', 'Code hash (first 12)', 'Name', 'Name key', 'Devices', 'First login (ISO)', 'Expires (ISO)', 'Last seen', 'Hash']); }

function setupSheets() { subSheet_(); redSheet_(); SpreadsheetApp.flush(); Logger.log('Sheets ready.'); }

function secret_() {
  var props = PropertiesService.getScriptProperties(), s = props.getProperty('UNSUB_SECRET');
  if (!s) { s = Utilities.getUuid() + Utilities.getUuid(); props.setProperty('UNSUB_SECRET', s); }
  return s;
}
function token_(email) {
  var raw = Utilities.computeHmacSha256Signature(email, secret_());
  return raw.map(function (b) { return ('0' + (b & 0xff).toString(16)).slice(-2); }).join('').slice(0, 32);
}
function unsubUrl_(email) { return CFG.SITE + '/unsubscribe.html?e=' + encodeURIComponent(email) + '&t=' + token_(email); }

function mail_(to, subject, text, html, listUnsub) {
  var opts = { name: CFG.FROM_NAME, replyTo: CFG.REPLY_TO, htmlBody: html };
  if (listUnsub) opts.headers = { 'List-Unsubscribe': '<' + listUnsub + '>' };
  try {
    var withFrom = {}; for (var k in opts) withFrom[k] = opts[k]; withFrom.from = CFG.FROM_EMAIL;
    GmailApp.sendEmail(to, subject, text, withFrom);      // works once updates@ is a verified "Send mail as" alias
  } catch (e) {
    delete opts.headers;                                  // MailApp does not accept custom headers
    MailApp.sendEmail(to, subject, text, opts);           // falls back to the script owner's own address
  }
}

function shell_(inner, email) {
  return '<div style="background:#0E0E10;padding:24px 12px;font-family:Arial,Helvetica,sans-serif">'
    + '<div style="max-width:560px;margin:0 auto;background:#16161A;border:1px solid #2a2a2e;border-radius:14px;padding:26px;color:#F0EDE6">'
    + '<div style="font-size:12px;letter-spacing:.12em;color:#C9A84C;font-weight:700;text-transform:uppercase;margin-bottom:14px">AI Made Simple School</div>'
    + inner
    + '<hr style="border:none;border-top:1px solid #2a2a2e;margin:22px 0 12px">'
    + '<div style="font-size:12px;color:#8A877F;line-height:1.6">You get this because you subscribed on aimadesimpleschool.com. '
    + '<a href="' + unsubUrl_(email) + '" style="color:#C9A84C">Unsubscribe</a> any time.<br>' + esc_(CFG.POSTAL) + '</div>'
    + '</div></div>';
}
function btn_(href, label) {
  return '<a href="' + href + '" style="display:inline-block;background:#C9A84C;color:#141210;text-decoration:none;font-weight:700;padding:12px 20px;border-radius:8px">' + label + '</a>';
}

/* ───────────────────────── 1. newsletter signup ───────────────────────── */

function subscribe_(p) {
  if (p.website) return { status: 'success' };           // honeypot: real people never fill this hidden field
  var email = String(p.email || '').trim().toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 120) return { status: 'error', message: 'Invalid email' };
  var lock = LockService.getScriptLock(); lock.waitLock(15000);
  var result = 'new';
  try {
    var sh = subSheet_(), data = sh.getDataRange().getValues();
    for (var i = 1; i < data.length; i++) {
      if (String(data[i][1]).toLowerCase() === email) {
        if (data[i][3] === 'Unsubscribed') { sh.getRange(i + 1, 4).setValue('Active'); sh.getRange(i + 1, 6).setValue(''); result = 'back'; break; }
        return { status: 'duplicate', message: 'Already subscribed' };
      }
    }
    if (result === 'new') sh.appendRow([stamp_(), email, String(p.source || 'Blog - Stay Ahead of AI').slice(0, 60), 'Active', String(p.track || '').slice(0, 30), '']);
  } finally { lock.releaseLock(); }
  try { sendWelcome_(email); } catch (e) { Logger.log('welcome failed: ' + e); }
  return { status: 'success', message: result === 'back' ? 'Welcome back' : 'Subscribed' };
}

function latestBrief_() {
  var res = UrlFetchApp.fetch(CFG.SITE + '/posts.json?cb=' + Date.now(), { muteHttpExceptions: true });
  if (res.getResponseCode() !== 200) return null;
  var posts = JSON.parse(res.getContentText()).filter(function (p) { return p.cat === CFG.BRIEF_CAT; });
  posts.sort(function (a, b) { return b.id - a.id; });
  return posts[0] || null;
}

function sendWelcome_(email) {
  var b = null; try { b = latestBrief_(); } catch (e) {}
  var inner = '<h1 style="font-size:24px;line-height:1.25;margin:0 0 10px;color:#fff">You\'re in. Welcome.</h1>'
    + '<p style="font-size:15px;line-height:1.7;color:#B8B5AE;margin:0 0 14px">Every Monday we send one short brief: what happened in AI this week, what it means for your work, and one thing to try.</p>'
    + (b ? '<p style="font-size:15px;line-height:1.7;color:#B8B5AE;margin:0 0 16px">Here is the latest one to start with:</p>' + btn_(CFG.SITE + '/blog.html?post=' + b.id, 'Read this week\'s brief') + '<br><br>' : '')
    + '<p style="font-size:15px;line-height:1.7;color:#B8B5AE;margin:0 0 16px">Want to use AI on your real work? Try Day 1 of the 30-Day AI Sprint free:</p>'
    + btn_(CFG.SITE + '/sprint-day1.html', 'Try Day 1 free');
  mail_(email, 'You\'re in: your weekly AI brief', 'Welcome to the AI Made Simple weekly brief. Read the latest: ' + CFG.SITE + '/blog.html', shell_(inner, email), unsubUrl_(email));
}

/* ───────────────────────────── 2. unsubscribe ───────────────────────────── */

function unsubscribe_(p) {
  var email = String(p.e || p.email || '').trim().toLowerCase();
  if (!email || String(p.t || '') !== token_(email)) return { status: 'error', message: 'Invalid link' };
  var sh = subSheet_(), data = sh.getDataRange().getValues();
  for (var i = 1; i < data.length; i++) {
    if (String(data[i][1]).toLowerCase() === email) {
      sh.getRange(i + 1, 4).setValue('Unsubscribed'); sh.getRange(i + 1, 6).setValue(stamp_());
      return { status: 'ok' };
    }
  }
  return { status: 'ok' };
}

/* ───────────────────────────── 3. weekly brief ───────────────────────────── */

/** Runs every morning (see installTriggers). Sends a new brief once, and resumes next day if the daily email quota ran out. */
function sendWeeklyDigest() {
  var props = PropertiesService.getScriptProperties();
  var b = latestBrief_(); if (!b) return;
  var id = String(b.id);
  if (props.getProperty('LAST_DIGEST_ID') === id) return;                 // already finished
  if (props.getProperty('CUR_DIGEST_ID') !== id) { props.setProperty('CUR_DIGEST_ID', id); props.setProperty('CUR_ROW', '2'); }
  var sh = subSheet_(), data = sh.getDataRange().getValues();
  var row = parseInt(props.getProperty('CUR_ROW') || '2', 10);
  var url = CFG.SITE + '/blog.html?post=' + b.id;
  var plain = b.title + '\n\n' + (b.excerpt || '') + '\n\nRead it: ' + url;
  for (; row <= data.length; row++) {
    var r = data[row - 1], email = String(r[1] || '').toLowerCase();
    if (!email || r[3] !== 'Active') continue;
    if (MailApp.getRemainingDailyQuota() < 2) { props.setProperty('CUR_ROW', String(row)); Logger.log('Quota used up; will resume tomorrow at row ' + row); return; }
    var inner = '<div style="font-size:12px;color:#8A877F;margin-bottom:6px">' + esc_(b.date || '') + ' · ' + esc_(b.rt || '') + ' read</div>'
      + '<h1 style="font-size:24px;line-height:1.25;margin:0 0 12px;color:#fff">' + esc_(b.title) + '</h1>'
      + '<p style="font-size:15px;line-height:1.7;color:#B8B5AE;margin:0 0 18px">' + esc_(b.excerpt || '') + '</p>'
      + btn_(url, 'Read the full brief')
      + '<p style="font-size:14px;line-height:1.7;color:#8A877F;margin:22px 0 0">Want to use AI on real work? <a href="' + CFG.SITE + '/sprint-day1.html" style="color:#C9A84C">Try Day 1 of the 30-Day AI Sprint free</a>.</p>';
    try { mail_(email, b.title, plain, shell_(inner, email), unsubUrl_(email)); } catch (e) { Logger.log('send failed for row ' + row + ': ' + e); }
  }
  props.setProperty('LAST_DIGEST_ID', id); props.deleteProperty('CUR_ROW'); props.deleteProperty('CUR_DIGEST_ID');
  Logger.log('Digest ' + id + ' sent.');
}

function installTriggers() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'sendWeeklyDigest') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('sendWeeklyDigest').timeBased().everyDays(1).atHour(9).create();   // 9am Lagos (set the project time zone!)
  Logger.log('Daily 9am check installed. A new brief is emailed the first morning it appears on the site.');
}

/* ───────────────────── 4. first-use access codes ───────────────────── */

function nameKey_(n) { return String(n || '').toLowerCase().replace(/[^a-z\s]/g, '').trim().split(/\s+/)[0] || ''; }

/** Starts the code's clock on first use. Same first name + up to MAX_DEVICES devices may keep using it. */
function redeem_(p) {
  var h = String(p.h || '').toLowerCase();
  if (!/^[0-9a-f]{64}$/.test(h)) return { status: 'unknown' };
  var no = VALID_HASHES.indexOf(h) + 1;
  if (no < 1) return { status: 'unknown' };
  var name = String(p.name || '').trim().slice(0, 60), key = nameKey_(name), dev = String(p.dev || '').replace(/[^a-z0-9]/gi, '').slice(0, 24);
  var lock = LockService.getScriptLock(); lock.waitLock(15000);
  try {
    var sh = redSheet_(), data = sh.getDataRange().getValues(), now = new Date();
    for (var i = 1; i < data.length; i++) {
      if (data[i][8] !== h) continue;
      var until = new Date(data[i][6]);
      if (data[i][3] && key && data[i][3] !== key) return { status: 'taken' };
      var devs = String(data[i][4] || '').split(',').filter(Boolean);
      if (dev && devs.indexOf(dev) < 0) { if (devs.length >= CFG.MAX_DEVICES) return { status: 'device_limit' }; devs.push(dev); sh.getRange(i + 1, 5).setValue(devs.join(',')); }
      sh.getRange(i + 1, 8).setValue(stamp_());
      if (now > until) return { status: 'expired', startedAt: new Date(data[i][5]).toISOString(), until: until.toISOString() };
      return { status: 'ok', startedAt: new Date(data[i][5]).toISOString(), until: until.toISOString() };
    }
    var end = new Date(now.getTime() + CFG.CODE_DAYS * 86400000);
    sh.appendRow([no, h.slice(0, 12), name, key, dev, now.toISOString(), end.toISOString(), stamp_(), h]);
    return { status: 'ok', startedAt: now.toISOString(), until: end.toISOString(), first: true };
  } finally { lock.releaseLock(); }
}

/** Refund or mix-up? Free the code so it can start again, e.g. resetRedemption(17). */
function resetRedemption(codeNo) {
  var sh = redSheet_(), data = sh.getDataRange().getValues();
  for (var i = data.length - 1; i >= 1; i--) if (Number(data[i][0]) === Number(codeNo)) sh.deleteRow(i + 1);
}
/** After a refund: end access today, e.g. revokeNow(17). */
function revokeNow(codeNo) {
  var sh = redSheet_(), data = sh.getDataRange().getValues();
  for (var i = 1; i < data.length; i++) if (Number(data[i][0]) === Number(codeNo)) sh.getRange(i + 1, 7).setValue(new Date(Date.now() - 1000).toISOString());
}

/* ───────────────────────────── tests ───────────────────────────── */

function testWelcome() { sendWelcome_('PUT-YOUR-EMAIL-HERE@gmail.com'); }
function testSubscribe() { Logger.log(doGet({ parameter: { email: 'test@example.com', source: 'Test' } }).getContent()); }
