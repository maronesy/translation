# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 585 (printed ٥٨٤)."""

PAGE_NUMBER = 585
PRINTED_PAGE = "٥٨٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «واستئناف سؤال آخر بـ«أم» المقدرة بالهمزة،» at the foot of PDF p. 584.
    {"type": "matn",
     "ar": "فإن قولك: «هل زيد عندك أم عمرو؟» في تقدير: «بل أعندك عمرو؟».",
     "en": "…for your saying “hal Zaydun ʿindaka am ʿAmrun?” is to be construed as “bal a-ʿindaka ʿAmrun?” (rather, is ʿAmr with you?)."},
    {"type": "matn",
     "ar": "(و) تقول: (﴿أثم إذا ما وقع﴾[[١]]، و﴿أفمن كان﴾[[٢]]، و﴿أومن كان﴾[[٣]]) بإدخال الهمزة على ثم، والفاء، والواو من الحروف العاطفة،",
     "en": "(And) you say: (“a-thumma idhā mā waqaʿa” (is it then, when it has come to pass), “a-fa-man kāna” (is he then who is), and “a-wa-man kāna” (or is he who was)), by placing the hamza before thumma, the fāʾ and the wāw among the coordinating particles,"},
    {"type": "matn",
     "ar": "(بخلاف «هل»)، لكونها فرع الهمزة، فلا تتصرف تصرفها.",
     "en": "(unlike “hal”), because it is a branch of the hamza, and so it does not have the range of use that the hamza has."},

    {"type": "section", "ar": "[حروف الشرط]",
     "en": "The Conditional Particles"},

    {"type": "matn",
     "ar": "(حروف الشرط: «إن»، و«لو»، و«أما». لها صدر الكلام.",
     "en": "(The conditional particles (ḥurūf al-sharṭ) are “in”, “law” and “ammā”. They take the head of the sentence (ṣadr al-kalām)."},
    {"type": "matn",
     "ar": "ف«إن»: للاستقبال، وإن دخل على الماضي، و«لو» عكسه)",
     "en": "“In” is for the future, even if it enters upon the past [tense], and “law” is the reverse of it.)"},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «فإن للاستقبال ولو للماضي».",
     "en": "In some copies: “for in is for the future and law is for the past.”"},
    {"type": "matn",
     "ar": "ومعناه: أن «إن» للاستقبال سواء دخلت على المضارع أو الماضي نحو: «إن تكرمني أكرمك» و«إن أكرمتني أكرمتك».",
     "en": "Its meaning is that “in” is for the future whether it enters upon the imperfect (muḍāriʿ) or the perfect (māḍī), as in “in tukrimnī ukrimka” (if you honour me, I shall honour you) and “in akramtanī akramtuka” (if you honoured me, I honoured you)."},
    {"type": "matn",
     "ar": "فمعنى المثال الثاني بعينه معنى المثال الأول، يعني: «إن وقع منك إكرامي في الاستقبال وقع مني أيضا إكرامك فيه».",
     "en": "The meaning of the second example is exactly the meaning of the first, namely: “if your honouring me occurs in the future, my honouring you will likewise occur in it.”"},
    {"type": "matn",
     "ar": "وكذلك «لو» للمضي على أيهما دخلت نحو: «لو ضربت ضربت، ولو تضرب أضرب» بمعنى واحد،",
     "en": "Likewise “law” is for the past, whichever of the two it enters upon, as in “law ḍarabta ḍarabtu” and “law taḍribu aḍribu”, with one and the same meaning,"},
    {"type": "matn",
     "ar": "أي: «لو وقع منك ضربي في الماضي فقد وقع مني ضربك أيضا فيه».",
     "en": "that is: “had your striking me occurred in the past, my striking you would likewise have occurred in it.”"},
    {"type": "matn",
     "ar": "وقد يستعمل «لو» ك«إن» في المستقبل نحو قوله تعالى: ﴿ولأمة مؤمنة خير من مشركة ولو أعجبتكم﴾[[٤]].",
     "en": "“Law” is sometimes used like “in” for the future, as in His words, the Exalted: “and a believing slave woman is better than a polytheist woman, even if she should please you.”"},
    {"type": "matn",
     "ar": "واعلم أن المشهور أن «لو» لانتفاء الثاني[[٥]] لانتفاء الأول، وهذا لازم معناه،",
     "en": "Know that the well-known view is that “law” is for the non-occurrence of the second [clause] because of the non-occurrence of the first; but this is a concomitant (lāzim) of its meaning,"},
    {"type": "matn",
     "ar": "فإنها موضوعة لتعليق حصول أمر في الماضي، لحصول أمر آخر مقدر فيه، وما كان",
     "en": "for it is coined (mawḍūʿa) to make the occurrence of one thing in the past dependent on the occurrence of another thing supposed in it; and whatever was…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يونس:٥١.",
     "en": "Qurʾān, Sūrat Yūnus 10:51."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: footnote ٢ prints «هود: ٨», but «أفمن كان على بينة من ربه» is Hūd 11:17; transcribed as printed.
    {"type": "pair",
     "ar": "هود: ٨.",
     "en": "Qurʾān, Sūrat Hūd 11:8 [translator’s reference: the phrase occurs at Hūd 11:17]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأنعام: ١٢٢.",
     "en": "Qurʾān, Sūrat al-Anʿām 6:122."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة البقرة: ٢٢١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:221."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ذهب المحقق التفتازاني إلى أن «لو» موضوعة لذلك،",
     "en": "The verifying scholar (al-muḥaqqiq) al-Taftāzānī held that “law” is coined for that;"},
    {"type": "pair",
     "ar": "فكأنه خالفه ليكون أدوات الشرط على نحو واحد في الوضع.",
     "en": "so it seems that he [the commentator] differed from him so that the conditional particles would be of a single pattern in their coining (waḍʿ)."},
]
