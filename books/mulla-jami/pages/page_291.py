# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 291 (printed ٢٩٠)."""

PAGE_NUMBER = 291
PRINTED_PAGE = "٢٩٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «و«كان هذا» from the foot of PDF p. 290.
    {"type": "matn",
     "ar": "زيد»، بخلاف المبتدأ والخبر، فإن الإعراب فيهما لا يصلح للقرينة، لاتفاقهما فيه، بل لا بد من قرينة رافعة للبس،",
     "en": "…Zayd”; unlike the mubtadaʾ and khabar, for inflection in them cannot serve as an indicator (qarīna), since they agree in it; rather, an indicator removing the ambiguity is necessary."},
    {"type": "matn",
     "ar": "وكذلك إذا انتفى الإعراب في اسم «كان» وخبرها جميعا ولا قرينة هناك لا يجوز تقديم الخبر، نحو: «كان الفتى هذا».",
     "en": "Likewise, when the inflection is absent in both the noun and the predicate of “kāna” and there is no indicator, placing the predicate first is not permitted, as in “This one was the youth.”"},
    {"type": "matn",
     "ar": "(وقد يحذف عامله) أي: عامل خبر «كان»، وهو «كان»[[١]]، لا خبر كان وأخواتها؛",
     "en": "(Its governor is sometimes elided), that is, the governor of the predicate of “kāna,” which is “kāna” itself—not of the predicate of kāna and its sisters;"},
    {"type": "matn",
     "ar": "لأنه لا يحذف من هذه الأفعال إلا «كان»، وإنما اختصت بهذا الحذف، لكثرة استعمالها",
     "en": "for of these verbs only “kāna” is elided, and it was singled out for this elision only because of its frequent use—"},
    {"type": "matn",
     "ar": "(في مثل: «الناس[[٢]] مجزيون بأعمالهم إن خيرا فخير وإن شرا فشر»).",
     "en": "(as in “People are requited for their deeds: if good, then good; and if evil, then evil”)."},
    {"type": "matn",
     "ar": "(ويجوز في مثلها) أي: في مثل هذه الصورة، وهي أن يجيء بعد «إن» اسم، ثم فاء بعده اسم (أربعة أوجه):",
     "en": "(In the like of it four ways are permitted), that is, in the like of this configuration, namely that a noun comes after “in” (if), and then a fāʾ followed by a noun:"},
    {"type": "matn",
     "ar": "١-نصب الأول ورفع الثاني: وهو أقواها، نحو: «إن خيرا فخير»، أي: «إن كان عمله خيرا فجزاؤه خير».",
     "en": "1. The accusative of the first and the nominative of the second, which is the strongest of them: as in “in khayran fa-khayrun,” that is, “if his deed was good, then his reward is good.”"},
    {"type": "matn",
     "ar": "٢-ونصبهما[[٣]]: نحو: «إن خيرا فخيرا» على معنى: «إن كان عمله خيرا فكان جزاؤه خيرا[[٤]]».",
     "en": "2. The accusative of both: as in “in khayran fa-khayran,” in the sense of “if his deed was good, then his reward was good.”"},
    {"type": "matn",
     "ar": "٣-ورفعهما: نحو: «إن خير فخير»، أي: «إن كان في عمله خير فجزاؤه خير».",
     "en": "3. The nominative of both: as in “in khayrun fa-khayrun,” that is, “if there was good in his deed, then his reward is good.”"},
    {"type": "matn",
     "ar": "٤-وعكس الأول: نحو: «إن خير فخيرا» أي: «إن كان في عمله خير فكان جزاؤه خيرا».",
     "en": "4. The reverse of the first: as in “in khayrun fa-khayran,” that is, “if there was good in his deed, then his reward was good.”"},
    {"type": "matn",
     "ar": "وقوة هذه الوجوه وضعفها بحسب قلة الحذف وكثرته.",
     "en": "The strength and weakness of these ways correspond to how little or how much is elided."},
    {"type": "matn",
     "ar": "(ويجب الحذف) أي: حذف عامله، يعني: «كان» (في مثل: «أما أنت منطلقا انطلقت») أي: لأن كنت منطلقا انطلقت،",
     "en": "(And elision is obligatory)—that is, the elision of its governor, meaning “kāna”—(in such as “ammā anta munṭaliqan inṭalaqtu”), that is, “because you were departing, I departed.”"},
    {"type": "matn",
     "ar": "فأصل: أما أنت: لأن كنت، حذفت اللام قياسا، ثم حذفت كلمة «كان» اختصارا، فانقلب الضمير المتصل منفصلا،",
     "en": "The origin of “ammā anta” is “li-an kunta”: the lām was elided by regular rule; then the word “kāna” was elided for brevity, so the attached pronoun turned into a detached one;"},
    {"type": "matn",
     "ar": "وزيدت لفظة «ما» بعد «أن» في موضع «كان» عوضا منها، وأدغمت النون في الميم، وأبقي الخبر على حاله،",
     "en": "the word “mā” was added after “an” in place of “kāna” as a compensation for it, the nūn was assimilated into the mīm, and the predicate was left as it was;"},
    {"type": "matn",
     "ar": "فصار «أما أنت منطلقا انطلقت»، وهذا على تقدير فتح الهمزة.",
     "en": "so it became “ammā anta munṭaliqan inṭalaqtu.” This is on the supposition that the hamza takes fatḥa."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أن إطلاقه ليس بجيد.",
     "en": "Meaning: his unqualified statement is not good."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: يحذف «كان» مع اسمها بعد «لو» وإن كان اسمها ضمير ما علم من غائب أو حاضر",
     "en": "Shaykh al-Raḍī said: “kāna” is elided together with its noun after “law” (even if) when its noun is the pronoun of something known, absent or present,"},
    {"type": "pair",
     "ar": "نحو: «اطلبوا العلم ولو بالصين» أي: ولو كان العلم بالصين،",
     "en": "as in “Seek knowledge, even in China,” that is, even if knowledge were in China;"},
    {"type": "pair",
     "ar": "وبعد لدن وأخواتها نحو: رأيتك لدن قائما، أي: لدن كنت قائما.",
     "en": "and after “ladun” and its sisters, as in “I saw you since standing,” that is, since you were standing."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يجوز في الثاني تقدير فعل لائق نحو: يجزي خيرا.",
     "en": "In the second, a suitable verb may be supposed, such as “he is requited with good.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إنما يصح دخول الفاء على الماضي؛ لأنه مقدر، والفعل المقدر لا بد له من الفاء.",
     "en": "The fāʾ may enter upon the past tense here only because it is supposed, and a supposed verb must have the fāʾ."},
]
