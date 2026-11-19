# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 154 (printed ١٥٣)."""

PAGE_NUMBER = 154
PRINTED_PAGE = "١٥٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "verse",
     "ar": "فخير نحن عند الناس منكم          ........................",
     "en": "“For better are we, in the people’s eyes, than you …” (the second hemistich is left as dots in the print)"},
    {"type": "matn",
     "ar": "فـ«خير» مبتدأ، و«نحن» فاعله[[١]]،",
     "en": "So “khayr” (better) is a mubtadaʾ, and “naḥnu” (we) is its agent;"},
    {"type": "matn",
     "ar": "ولو جعل «خير» خبرا عن «نحن» لفصل بين اسم التفضيل ومعموله الذي هو «من» بأجنبي، وهو غير جائز لضعف عمله،",
     "en": "had “khayr” been made the khabar of “naḥnu,” the elative (ism al-tafḍīl) would be separated from its governed element, which is “min,” by an extraneous element (ajnabī), and that is not permissible because of the weakness of its government;"},
    {"type": "matn",
     "ar": "بخلاف ما لو كان فاعلا، لكونه كالجزء",
     "en": "unlike if it were an agent, because [the agent] is like a part [of its governor]."},
    {"type": "matn",
     "ar": "(رافعة لظاهر) أو ما يجري مجراه[[٢]]. وهو الضمير المنفصل لئلا يخرج عنه قوله تعالى: ﴿أراغب أنت عن آلهتي﴾[[٣]].",
     "en": "(Putting an overt noun in the nominative—rāfiʿatan li-ẓāhirin), or what is treated like it, namely the detached pronoun, so that His words, the Exalted, are not excluded from it: “Are you averse to my gods?” (Qurʾān, Sūrat Maryam 19:46)."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «أقائمان الزيدان»؛ لأن «أقائمان» رافع لضمير عائد إلى «الزيدان»، ولو كان رافعا لهذا الظاهر لم يجز تثنيته[[٤]].",
     "en": "By it he excluded such as “a-qāʾimāni al-Zaydāni” (Are the two Zayds standing?), because “a-qāʾimāni” governs in the nominative a pronoun referring to “al-Zaydāni”; had it governed this overt noun, its dualization would not be permissible."},
    {"type": "matn",
     "ar": "(مثل: زيد قائم) مثال للقسم الأول من المبتدأ.",
     "en": "(Like: Zayd is standing—mithlu: Zaydun qāʾimun): an example of the first kind of mubtadaʾ."},
    {"type": "matn",
     "ar": "(وما قائم الزيدان) مثال للصفة الواقعة بعد حرف النفي.",
     "en": "(And the two Zayds are not standing—wa-mā qāʾimun al-Zaydāni): an example of the adjective occurring after a particle of negation."},
    {"type": "matn",
     "ar": "(وأقائم الزيدان) مثال للصفة الواقعة بعد حرف الاستفهام.",
     "en": "(And are the two Zayds standing?—wa-a-qāʾimun al-Zaydāni): an example of the adjective occurring after a particle of interrogation."},
    {"type": "matn",
     "ar": "(فإن طابقت) أي: الصفة الواقعة بعد حرف النفي وألف الاستفهام[[٥]] اسما (مفردا) مذكورا بعدها نحو: «ما قائم زيد، وأقائم زيد».",
     "en": "(Then if it agrees—fa-in ṭābaqat), that is: the adjective occurring after the particle of negation and the alif of interrogation, with a (singular—mufradan) noun mentioned after it, as in: “Zayd is not standing” (mā qāʾimun Zaydun) and “Is Zayd standing?” (a-qāʾimun Zaydun)—"},
    # NOTE: «ليس» is printed in guillemets; read as the idiom «ليس إلا» ("nothing else").
    {"type": "matn",
     "ar": "واحترز به عما إذا طابقت مثنى، نحو: «أقائمان الزيدان» أو مجموعا نحو: «أقائمون الزيدون»، فإنها حينئذ خبر «ليس» إلا",
     "en": "by it he excluded where it agrees with a dual, as in “a-qāʾimāni al-Zaydāni,” or a plural, as in “a-qāʾimūna al-Zaydūna” (Are the Zayds standing?), for then it is a khabar and nothing else—"},
    {"type": "matn",
     "ar": "(جاز الأمران[[٦]]) كون الصفة مبتدأ، وما بعدها",
     "en": "(both options are permissible—jāza al-amrāni): the adjective’s being a mubtadaʾ and what follows it…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه نظر لانحصار كون فاعل اسم التفضيل اسما ظاهرا في مسألة الكحل،",
     "en": "This is open to examination, because the agent of the elative being an overt noun is confined to the “kuḥl” question (masʾalat al-kuḥl);"},
    {"type": "pair",
     "ar": "فتعين كون «نحن» مبتدأ، وكون «منكم» مفسرا لمحذوف تقديره: \"فخير منكم نحن عند الناس\"، فلما حذف فسر بقوله: \"منكم\".",
     "en": "so “naḥnu” must be the mubtadaʾ, and “minkum” an explication of something elided, the implied form being: “For better than you are we in the people’s eyes”; when it was elided, it was explicated by his words “minkum.”"},
    {"type": "pair",
     "ar": "ولو صح ما ذكره لصح «أخير نحن»، فينتقض قاعدة جواز الأمرين به؛",
     "en": "Had what he mentioned been valid, “a-khayrun naḥnu” (Are we better?) would be valid, and the rule of the permissibility of both options would be broken by it;"},
    {"type": "pair",
     "ar": "لأنه من جواز الأمرين، وقد خرج من القاعدة؛ لأن «خيرا» ليس مطابقا لمفرد، فافهم.",
     "en": "for it belongs to [the case of] the permissibility of both options, yet it has left the rule, because “khayr” does not agree with a singular—so understand."},
    {"type": "pair",
     "ar": "وبعد يرد انتقاض القاعدة بقولنا: «أخير منكم عند الناس».",
     "en": "Further, the rule is open to being broken by our saying: “a-khayrun minkum ʿinda al-nāsi.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بتقدير المعطوف أو من باب عموم المجاز.",
     "en": "By supposing an [elided] conjunct, or by way of the generality of the figurative (ʿumūm al-majāz)."},
    {"type": "pair",
     "ar": "ولك أن تريد بالظاهر معناه اللغوي، أي: البارز.",
     "en": "You may also take “overt” (ẓāhir) in its lexical sense, that is: visible (bāriz)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة مريم: ٤٦.",
     "en": "Qurʾān, Sūrat Maryam 19:46."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "على اللغة المشهورة.",
     "en": "According to the well-known usage."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "نبه بهذا على أن ضمير «طابقت» لم يرجع إلى الصفة المذكورة بجميع أوصافها،",
     "en": "By this he indicated that the pronoun of “ṭābaqat” does not refer to the adjective mentioned with all of its qualifications;"},
    {"type": "pair",
     "ar": "فإنه لم يعتبر ههنا كونها رافعة لظاهر، فإنها لو كانت رافعة لظاهر لم يصح جعلها خبرا.",
     "en": "for its governing an overt noun in the nominative is not taken into account here, since were it governing an overt noun, making it a khabar would not be valid."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قيل: لو كان «زيد» مبتدأ ينبغي ألا يجوز «أقائم زيد؟»؛ لأنه يلزم تقديم الخبر مع أنه يوجب الالتباس بالفاعل كما في «زيد قام»؟",
     "en": "It has been said: if “Zayd” were a mubtadaʾ, “a-qāʾimun Zaydun?” ought not to be permissible, because it would entail fronting the khabar although that causes confusion with the agent, as in “Zayd stood” (Zaydun qāma)?"},
    {"type": "pair",
     "ar": "وأجيب: بأن «قام زيد» يتعين فيه كون «زيد» فاعلا بحيث يختفي احتمال كونه مبتدأ بالمرة، لأنه لا يشتمل على خلاف الأصل بخلاف كونه مبتدأ، فيلتبس المقصود التباسا شديدا،",
     "en": "It was answered that in “qāma Zaydun” (Zayd stood) “Zayd” is determined as agent, such that the possibility of its being a mubtadaʾ disappears entirely, since [that reading] involves nothing contrary to the norm, unlike its being a mubtadaʾ; so the intended [sense] would be severely confused;"},
    {"type": "pair",
     "ar": "بخلاف «أقائم زيد؟»، فإن الفاعلية يشتمل على كون «قائم» مبتدأ على خلاف الأصل، وكونه مبتدأ يشتمل على تقديم الخبر على خلاف الأصل،",
     "en": "unlike “a-qāʾimun Zaydun?,” for the agent reading involves “qāʾim” being a mubtadaʾ contrary to the norm, and its [Zayd’s] being a mubtadaʾ involves fronting the khabar contrary to the norm;"},
    {"type": "pair",
     "ar": "فلا يختفي المقصود بسبب كون خلافه أظهر كل",
     "en": "so the intended [sense] is not hidden on account of its alternative being more evident in every…"},
]
