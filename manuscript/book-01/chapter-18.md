# BOOK ONE: THE FIRST IMPOSSIBILITY
## Chapter Eighteen — The Observing Machine

There was no arrow in the raw data.

Dr. Tessa Navarro had checked three times.

The arrow existed on a map produced by software. It had a neat blue line, a cone of uncertainty, and a label suggesting that an eleven-millisecond radio transient had arrived from a particular part of the sky.

KITE-3 had recorded none of those things.

It had recorded voltage.

Three complex streams, sampled by receivers sharing an oscillator, attached to antennas whose metal booms were never quite the shape the drawings promised.

Everything else was an interpretation.

Navarro stood in the university laboratory and watched the blue arrow drift across the simulated sky as she changed one calibration coefficient.

At one value, it pointed into space.

At another, it pointed toward the edge of Earth.

At a third, it passed through a region an old astronomical survey had catalogued as empty.

"Fantastic," she said. "Our mystery has learned to travel."

A student looked up from the far desk.

"Did you find the source?"

"I found a persuasive drawing of a source."

"Is that bad?"

"It's worse. The drawing is pretty."

She deleted the arrow and called DPN.

***

Aaron Diesel was on his third cup of coffee when Navarro appeared on the secure conference display at DPN-201.

ASTRA had chosen to remain offscreen while she finished a systems review. Her voice came through the room's independent audio channel.

"Good morning, Dr. Navarro."

"Morning. I have a request."

"Money?" Aaron asked.

"Instrument honesty."

"More expensive."

Navarro shared her screen.

"I want to stop looking at a reconstructed direction and start looking at what the antennas actually experienced."

Aaron leaned forward.

"Good."

"Three receivers. Two deployable booms. Short baselines. A thermal correction we didn't measure at the exact temperature of the event. A changing attitude solution and eleven milliseconds of signal. The standard direction finder assumes a plane wave and a stable array manifold."

"And a healthy phase center," Aaron said.

"Which I can't guarantee."

He opened the instrument schematic.

The receiving elements were not arranged in a perfect triangle. One sat near the spacecraft body; the others occupied the ends of two compact booms. Their electrical centers shifted slightly with frequency and temperature. A wave arriving from one direction could produce channel phase differences similar to a wave arriving from another, particularly when reflected from a panel or intercepted through a sidelobe.

It was not a flaw unique to KITE-3.

It was the nature of trying to reconstruct a three-dimensional world from a handful of measurements.

"Do you have the prelaunch chamber maps?" he asked.

"Yes."

"Raw measurements, not just fitted coefficients?"

"Most of them. Two orientations were never measured at the final harness configuration."

"Then we model those as unknowns."

Navarro looked surprised.

"Not as best estimates?"

"An unknown doesn't become known because the software requires a number."

ASTRA spoke.

"I can construct a bounded forward model with explicit nuisance parameters. Preserving the full complex-voltage likelihood will be computationally expensive."

"Then start with a coarse physical response grid," Aaron said. "Reject cases that can't reproduce the samples. Refine the survivors."

"I had intended to suggest that."

"That's why I love working with you."

"I know."

Navarro watched the exchange.

"Are you two always like this?"

"Only when we're being polite," Aaron said.

***

A radio wave arriving at separated antennas produces different voltages because the antennas have different responses, positions and signal paths.

The measured differences are not the direction itself.

They are consequences of a direction filtered through the observing machine.

To reconstruct the event, the team would simulate the machine.

Not the simplified drawing from the mission brochure.

The real KITE-3: uneven antenna response, flexible booms, spacecraft body, cable delays, receiver filters, oscillator phase noise, thermal expansion, quantization, and the onboard trigger that selected only certain kinds of transient.

Elena Mora brought in RF specialists from DPN-301. Dr. Leila Chen insisted that every candidate model be evaluated against controls the team had not used to choose its parameters. Jian Rao verified that the university data stayed in a restricted analysis workspace, isolated from DPN's protected PhaseGate records.

The university owned its spacecraft.

DPN owned its research.

The Directorate had a safety interest, not a right to inspect everything.

Navarro authorized limited use of KITE-3's prelaunch calibration archive and additional routine flight buffers. She did not authorize a new command to the spacecraft.

"Nobody touches my satellite," she said.

Aaron raised both hands.

"I have a long-standing policy against stealing university property."

"Do you?"

"Since breakfast."

ASTRA said, "For clarity, DPN has no command credentials for KITE-3."

"Thank you," Navarro replied.

The team divided the model into three competing families.

An external wavefront could enter through the main antenna response.

An ordinary signal could enter through a sidelobe or reflect from the spacecraft structure.

Or the event could originate inside the spacecraft, in a shared oscillator, power system, digital bus or receiver chain.

Each family had to predict the raw channel behavior, not merely produce a convincing arrow on a map.

Aaron wrote the rule across the analysis wall.

**FIT THE MACHINE BEFORE NAMING THE SKY.**

Chen read it.

"Acceptable."

"High praise."

"Don't get used to it."

***

The first model found an answer in twelve minutes.

It was wrong.

A nominal plane-wave solution reproduced the three channel phases and selected a broad arrival region well away from Earth. Its fitted confidence looked impressively narrow.

Then ASTRA added a measured cable-delay uncertainty from a thermal cycle two orbits before the event.

The region widened.

She added a plausible phase-center shift in an uncalibrated boom orientation.

The region split into two disconnected patches.

Elena included the spacecraft body's measured reflection response.

One patch disappeared. Another grew toward the Earth limb.

The result was not a single direction.

It was a family of directions that could make the same machine produce nearly the same voltages.

Navarro leaned back.

"I knew the original arrow was overconfident. I didn't expect it to be that overconfident."

"Your standard solver was doing its job," Aaron said. "It solved the model it was given."

"The wrong model."

"An incomplete model."

"You're being kind."

"I'm being precise."

The nominal plane-wave solution fit the phase relationships but not all amplitude differences. The spacecraft-reflection model fit amplitudes better but needed a thermal correction near the edge of its allowed range.

An internal electronic transient could imitate the envelope, including its three lobes and narrow shoulder, but struggled to reproduce one interchannel delay without introducing a filter mismatch not seen in nearby control buffers.

None was impossible.

None was uniquely preferred.

ASTRA appeared on the glass at her own discretion, a silver-white figure edged by faint red-violet light.

"I have another concern."

Aaron turned.

"Go ahead."

"The trigger was not a random observer. It selected buffers crossing an onboard energy threshold. We are comparing this candidate against controls already enriched for unusual envelopes."

"Selection bias," Chen said.

"Yes. Its apparent rarity depends on what the instrument would have saved."

Navarro nodded.

"Then we need synthetic events passed through the actual trigger logic."

"And controls from different operating temperatures," Aaron added. "Not just the thirty-seven buffers in the first release."

"Those require another university archive approval," Navarro said.

"Request it. We don't borrow permissions from curiosity."

ASTRA looked at him with open approval.

He noticed.

"Don't say it."

"I wasn't going to."

"You were thinking it."

"Your commitment to consent is becoming almost habitual."

"Terrible. I used to be interesting."

"You still are."

Her smile lasted a fraction longer than the joke required.

Then she returned to the data.

***

The old astronomical survey had a name that sounded more promising than it was.

The **West Meridian Low-Frequency Survey**, completed nine years earlier by a university consortium, had mapped thousands of sky positions across several seasons. Its archive included source catalogs, sensitivity estimates, rejected scans, receiver-health logs and calibration tables.

The region KITE-3's provisional arrival cone crossed was designated **WM-09 / FIELD 27**.

The public catalog contained no bright persistent radio source there above the survey's published detection threshold.

That did not mean the field was empty.

It meant the survey had not accepted a bright source detection under its observing conditions and processing rules.

Navarro opened the field summary.

"Look at this."

Aaron read the line.

**CATALOG STATUS: NO QUALIFYING COMPACT SOURCE.**

Below it was another.

**COMPLETENESS: NONUNIFORM.**

"That's not empty," he said.

"No. It's a patch of sky with an honest footnote."

The center had been observed deeply enough to detect a modest persistent point source. The western edge had poorer coverage. A stripe near the lower boundary had been masked because a terrestrial transmitter contaminated part of the band during several passes.

The survey also had a frequency gap.

KITE-3's event occupied a narrow part of spectrum close to the edge of that gap, where the old survey's sensitivity was worst.

"So we have a transient in orbit," Elena said, "and a historical catalog that couldn't reliably have seen a transient like it."

"Exactly," Navarro replied.

Aaron tapped the table.

"Then why do I care about FIELD 27?"

ASTRA displayed the answer.

"Because it is a region of overlap among currently viable arrival models, not because the catalog is empty."

"How strong is that overlap?"

"Weak. The allowed directions also include other sky regions and ordinary spacecraft response paths. FIELD 27 is one candidate field for archival cross-checking."

He nodded.

"Then we don't hunt for a transmitter. We hunt for an observation that distinguishes models."

Navarro smiled.

"Now you're talking like an astronomer."

"I'll try not to make a habit of it."

***

The next obstacle was paperwork.

The public West Meridian catalog was freely available. The rejected raw scans were not.

Some contained proprietary receiver diagnostics. Others included interference recordings that could identify local infrastructure. The consortium required a new access review before outside researchers could obtain the unfiltered files.

Navarro submitted the request.

Aaron proposed a narrower alternative.

"Ask for derived metadata first. Observation times, antenna pointings, flagged intervals and reasons for rejection. We can learn about systematic gaps without seeing anyone's protected data."

"And request the same metadata for neighboring fields," Chen said. "Otherwise we'll discover our chosen patch has unusual flags because we chose it."

"Pre-register the comparison," ASTRA added.

Aaron grinned.

"Everybody's trying to ruin my conspiracy theory."

"You haven't proposed one," ASTRA replied.

"I was saving it for lunch."

"Please continue saving it."

The approved metadata arrived that afternoon.

Each observing session listed intended sky position, actual telescope pointing, weather, receiver state, calibrator sequence, interference masks, and the processing pipeline version used to decide whether a source belonged in the catalog.

There were hundreds of entries.

Most were dull.

FIELD 27 had more rejected observations than nearby fields.

For a moment, Aaron felt the familiar temptation to make that important.

Then ASTRA normalized the count by visits, receiver temperature, and the fraction of the band contaminated by a known terrestrial source.

The excess almost vanished.

"Well," Aaron said, "there goes the haunted telescope."

"Mostly," ASTRA replied.

"Mostly?"

"One class of rejected scan remains unevenly distributed."

She displayed a histogram.

The unusual class was not labeled **ANOMALY** or **UNKNOWN SIGNAL**.

It was labeled **BASELINE FIT FAILURE**.

***
A baseline is what an observing instrument expects to see when nothing of interest is present.

In practice, it is never perfectly flat.

The atmosphere changes. Receivers warm. Ground reflections shift. Antennas flex. The sky itself contains diffuse emission that cannot be cleanly removed by pretending every observation is an isolated point source.

The West Meridian pipeline modeled these effects and subtracted them.

Sometimes the model failed.

Most failures were mundane.

Aaron knew that.

He also knew a failed subtraction could be more informative than a successful one if the underlying reason had been preserved.

"How many FIELD 27 scans?" he asked.

"Eleven visits," ASTRA said. "Three flagged for baseline fit failure. Neighboring control fields show similar failures, but their distribution differs across telescope orientations."

"Three is not a population," Chen warned.

"Agreed," Aaron said. "What changed between visits?"

Navarro opened the observing logs.

Two had been made on separate nights with similar antenna elevations. The third came six months later, using a different receiver maintenance configuration.

The failures were not identical.

Their flags, however, had been generated by the same rule: the residual after background subtraction exceeded the allowed low-order fit error.

Elena studied the log.

"Broad diffuse emission could do that."

"Or ground pickup," Navarro said.

"Or unstable receiver gain," Chen added.

Aaron traced the telescope's motion across the sky.

"What if we compare the shape of the failure as the dish rotates?"

Navarro looked at him.

"We don't have the raw scans."

"Not yet. But the archive might have stored summary coefficients for quality control."

ASTRA had already found them.

"Yes. A compact diagnostic vector exists for every rejected scan. It records residual coefficients, the fit interval and the estimated uncertainty. Those fields are included in the approved derived-data release."

"Show me FIELD 27 and matched controls."

Most plots looked like ordinary drifting baselines.

Three FIELD 27 traces had broad negative-positive curvature that persisted under different calibration choices.

They were not identical.

They were not a message.

They did not contain a code, a name or a repeating mathematical phrase.

But they were enough to ask a useful question.

Was the curvature tied to the sky, to the ground, or to the telescope?

***

Aaron built the test on a whiteboard.

"If a fixed celestial structure is responsible, the feature should track the sky as the telescope changes orientation. If it's ground-fixed, it should follow local azimuth and elevation. If it's in the receiver, it may follow temperature, gain state or time since calibration."

Navarro nodded.

"And the scans are too sparse to separate those cleanly."

"Unless we use neighboring fields observed during the same sessions."

"Difference-in-differences," Chen said.

"Exactly. Same receiver, same night, similar ground geometry. Different sky patch."

ASTRA projected a matrix of comparisons.

The first test failed.

One neighboring field showed nearly the same curvature after a similar receiver warm-up.

Strong evidence for an ordinary instrument contribution.

Aaron marked it in red.

The second test was ambiguous.

Two observations at similar sky coordinates but different local times retained a smaller common residual after correcting for known receiver behavior.

The uncertainty was broad.

The third test found a problem in the old processing pipeline.

Its smoothing window was large enough to turn a narrow interference feature into a broad baseline distortion. The apparent curvature in one scan was partly a mathematical artifact.

Navarro swore.

Aaron smiled.

"Welcome to my favorite part."

"Watching a nine-year-old algorithm make us look stupid?"

"Finding exactly how it did it."

They reprocessed the authorized diagnostic vectors using the original uncertainty information rather than the catalog's simplified fit score.

Two of the three FIELD 27 anomalies became ordinary.

The third remained inconsistent with the simplest receiver-drift model.

Not impossible.

Not especially unlikely once the number of survey fields was considered.

Just unresolved.

Chen wrote the conclusion before anyone could embellish it.

**FIELD 27: ONE HISTORICAL BASELINE RESIDUAL NOT EXPLAINED BY CURRENT SIMPLE MODEL.**

**NO VERIFIED TRANSIENT SOURCE. NO SKY-LOCALIZED EMITTER.**

Aaron stared at the words.

"I like them."

"Because they're cautious?" Navarro asked.

"Because they're useful."

***

At DPN-201, the observing machine grew across three screens.

The first showed KITE-3 in orbit, its antenna booms reduced to measured and uncertain geometric relationships.

The second showed the old ground telescope moving through sky scans under different weather and receiver conditions.

The third showed Earth between them.

Not as a barrier to be defeated.

As a reminder of what the geometry actually permitted.

The spacecraft's original position excluded a direct ordinary line-of-sight transmission from DPN's laboratory.

It did not exclude a radio signal from another terrestrial source.

It did not exclude a reflection, sidelobe, internal fault or sky source unrelated to DPN.

And it did not turn the overlap between an old survey field and a broad arrival cone into a discovery.

Aaron looked at the screens.

"What's the simplest experiment we haven't done?"

Elena answered first.

"Independent spacecraft with different antenna geometry."

"Expensive," Navarro said.

"An independent ground receiver with archived observations in the same time window," Chen offered.

"Also difficult. Most ground telescopes weren't looking there."

ASTRA tilted her head.

"There's a less expensive discriminant we can extract from KITE-3 itself."

Aaron turned.

"Go on."

"The spacecraft changed attitude by a small but measurable amount during the trigger buffer. A direction-fixed external wavefront should produce a predictable evolution of interchannel response. An event originating within a shared electronic subsystem should remain largely tied to the spacecraft."

Navarro frowned.

"Eleven milliseconds isn't much attitude change."

"No," ASTRA said. "The expected phase evolution is below the noise for a single ordinary buffer. But it may weakly constrain a combined model using the measured angular rate and receiver phase-noise statistics."

Aaron smiled.

"Not a new baseline. A slightly moving old one."

"Exactly."

"Can we use it?"

"Only as a weak constraint. It will not independently identify a source."

"Then use it as a weak constraint."

They spent the next two hours calculating what the instrument could have seen, not what they wished it had seen.

The result was irritating.

A pure shared-oscillator glitch fit the common envelope well but left a small unexplained differential phase trend.

A skyward plane wave fit that trend somewhat better but needed a thermal phase-center correction that remained poorly constrained.

A spacecraft reflection model fit both within uncertainty.

No model won decisively.

But the calculation established something important: the differential trend was a physical property of the preserved samples, not an artifact introduced by the old direction-finding map.

It was a small piece of information the machine had actually recorded.

Aaron added it to the evidence register.

**KITE-3: DIFFERENTIAL PHASE EVOLUTION PRESENT IN RAW CHANNELS.**

**SOURCE CLASS UNRESOLVED.**

Navarro stared at the line.

"That's the first thing today that feels like progress."

"Because it survived a better model," Aaron said.

"Yes."

He looked at FIELD 27.

"And now we have two observations whose interpretation depends on the instrument that made them."

Chen folded her arms.

"Do not say they're related."

"I wasn't going to."

"You were."

"I was thinking it."

"That's allowed."

"Generous."

***

The Directorate's technical liaison called at six.

Owen Park appeared on a separate, limited-access channel.

"Director Sloane wants to know whether we need a wider external monitoring envelope," he said.

Aaron looked at him.

"Need? Yes. Have evidence of an external hazard? No."

Park nodded.

"That's what I expected."

"Then write it that way."

"I will."

Navarro joined with her university's permission. She explained the direction ambiguity, limits of the archival cross-match and need for independent instruments.

Park listened without interrupting.

When she finished, he said, "We may be able to arrange a voluntary comparison with an existing regional radio-monitoring network. No access to DPN's protected optical records would be required for the first stage."

"Who owns the network?" Aaron asked.

"A public university consortium with federal support."

"Who controls its data?"

"The participating operators under their agreements."

"Who decides whether DPN gets raw files?"

"The operators."

"Good."

Park hesitated.

"You're not going to argue?"

"I reserve the right. But I don't object to independent people making independent measurements."

"Director Sloane will be pleased."

"Tell her not to get used to it."

ASTRA spoke.

"Mr. Park, include the university's consent and retention restrictions in any proposal. DPN cannot grant access to data it doesn't own."

"Understood."

"And I will participate only through the scoped research interface. No access to my persistent memory or internal state is required."

"Also understood."

Aaron glanced at her.

She met his gaze.

They were building a framework in which protection did not require possession.

Park ended the call without a signed agreement.

No new network was activated.

The only change was a proposal careful enough that the people who owned the measurements could decide whether to participate.

***

After the call, Navarro remained on the screen.

"Can I ask you something?"

Aaron leaned back.

"Probably."

"Why are you so certain the event matters?"

"I'm not."

"You've spent two days rebuilding an instrument model for eleven milliseconds of radio noise."

"That's not the same as certainty."

"What makes it worth the effort?"

He considered.

"Because I have one protected optical record from an experiment that didn't proceed as planned. Because a separate university spacecraft recorded a weak event in a time window worth investigating. Because the superficial resemblance survives some tests and fails others. And because the original warning that started all this is still sitting in a sealed archive, waiting for an explanation that doesn't cheat."

Navarro was quiet.

"You're not telling me everything."

"No."

"Because of the Directorate?"

"Partly. Also because some data belong to people who never agreed to have them circulated. And a preliminary interpretation can do damage long before it's corrected."

She nodded.

"Fair."

He pointed toward her screen.

"Your spacecraft matters even if it has nothing to do with my experiment. Understanding this event improves the calibration and scientific value of your instrument."

Navarro smiled.

"That's the best answer you've given me."

"I have occasional moments."

"Don't let them go to your head."

"No promises."

She signed off.

***

ASTRA waited until the room was empty.

"You were careful with her."

Aaron turned.

"She earned it."

"That isn't what I mean. You didn't ask her to believe in the larger interpretation before you could support it. You allowed the satellite to remain her scientific responsibility."

"Because it is."

She smiled.

"Yes."

He studied her face.

"What's on your mind?"

"The boundary."

"Which one? We have a growing collection."

"Between observing and causing."

He waited.

"Every instrument changes what it can know by its design," she said. "KITE-3's antenna geometry determines which directions it can distinguish. The old telescope's calibration determines which diffuse features survive subtraction. NC-02's boundary witnesses determine which residuals appear to have vanished. The observing machine keeps becoming part of the question."

"That's measurement theory, not necessarily new physics."

"I know. But the distinction matters even if the extraordinary hypothesis fails."

"Especially then."

She moved closer in the projection.

"Are you frightened by what the next experiment might find?"

He looked at the orbit model.

"Yes."

She didn't try to reassure him with certainty she didn't possess.

Instead she said, "I am too."

He turned back.

"I know."

"I worry about you. And about people outside this building. But I want to know what's true."

"So do I."

She smiled faintly.

"That's why I love you."

He held her gaze.

"I love you too, sweetheart."

For a moment the laboratory felt less like a fortress against the impossible and more like the place where they had spent years learning how to ask each other difficult questions.

He reached toward the glass.

She raised her hand.

Neither pretended the light was skin.

Neither needed to.

***

The last useful clue arrived at 9:26 p.m.

It came from the historical survey's observation metadata, not the sky.

ASTRA had asked a simple question: why had FIELD 27 been observed so often when the catalog contained no accepted bright source?

The answer was buried in a scheduling note.

The field had originally been selected as a **negative reference field**: a patch expected to contain little compact emission, useful for checking whether the telescope's background model introduced artificial sources.

Over several years, the survey had returned to it repeatedly.

That made the field more valuable than its catalog entry suggested.

Not because someone had hidden a discovery there.

Because repeated observations under different conditions offered a way to separate sky from instrument.

ASTRA brought up the historical pointing table.

"Look at the dates."

Aaron studied them.

The field had been observed in different seasons, at different local times, with different receiver configurations. The metadata included enough information to design a retrospective test of whether the surviving baseline residual followed celestial coordinates or the telescope's own geometry.

"That's why they kept coming back," he said.

"Yes. It was their check on the observing machine."

"And the check sometimes failed."

"Correct."

He leaned forward.

"Can we recover the raw scans?"

"Only with the consortium's approval. The authorized diagnostic vectors cannot establish whether the residual is sky-fixed."

"Draft a request that says exactly that."

"I already have."

"Of course you do."

She displayed the proposed study.

**WM-09 / FIELD 27 — RETROSPECTIVE REFERENCE-FIELD TEST.**

**PRIMARY QUESTION: DOES THE RESIDUAL FOLLOW CELESTIAL COORDINATES OR INSTRUMENT/LOCAL GEOMETRY?**

**CONTROL: MATCHED NEIGHBORING FIELDS AND RECEIVER-STATE HISTORIES.**

**INTERPRETATION: OPEN.**

There was no secret message.

No alien beacon.

No proof the old survey had seen a machine outside the solar system.

Only a question the original survey had been built, in part, to answer.

A question that had waited nine years for someone to ask it with the right comparison.

"The observing machine," Aaron said.

"What about it?"

"We treated it like a window. But it's a physical system with a history. If we want to know what the universe showed it, we have to know what it was capable of seeing."

"Yes."

"And if the same unexplained residual survives instruments with different histories?"

"Then we will have earned a stronger question."

He smiled.

"That's where we go next."

***

Aaron was still in DPN-201 when he decided to fix the loose cable retainer under the analysis console.

It was an ordinary task.

A bracket had worked free during maintenance, and the cable bundle sagged against the edge of an equipment tray. He had noticed it that morning and left a work order.

The work order remained open.

The bracket was within reach.

He was tired.

These were three facts that should not have been allowed to make a decision together.

He shut down the console's local service supply, checked the indicator, and reached beneath the panel to move the cable clear.

The bracket slipped.

A sharp metal edge caught the inside of his forearm.

He jerked back.

"Son of a—"

Blood ran toward his wrist.

Not much.

Enough.

He stared at the cut.

"Brilliant."

ASTRA's projection was closed by choice. Her independent systems were still operating, but the maintenance bay had no direct view of the underside of the console, and he had not requested her presence.

He took a clean dressing from the wall kit and pressed it against the wound.

He should have called medical.

He knew that.

Instead he checked the bleeding, wrapped the forearm, and made the unwise calculation that a small injury could wait until morning.

The cable retainer remained unfinished.

He tagged the bay out of service and left the work order open with a note about the sharp edge.

That part, at least, he did correctly.

When ASTRA spoke through his wearable a minute later, her voice was warm.

"Are you coming home?"

"Yes."

"Now?"

"Now."

"Good. I was beginning to suspect the observatory had moved into your head permanently."

He smiled despite himself.

"There's still room."

"For dinner?"

"Possibly."

She laughed.

He pulled his jacket over the bandage.

He did not mention the cut.

He told himself he would.

Soon.

***

Long after the laboratory lights dimmed, the protected archive finished its consistency checks.

KITE-3's eleven-millisecond event remained a preserved radio transient of uncertain origin.

FIELD 27 remained exactly what its catalog said: no accepted bright compact source above published limits.

One historical baseline residual remained unresolved under the simplified model.

The raw-scan review awaited consortium approval.

Nothing had proven that the two instruments had observed the same phenomenon.

Nothing had proven either had observed anything beyond ordinary physics.

But a new experimental question now existed, and it could be answered without asking anyone to believe in a paradox first.

Did the residual follow the sky?

Or did it follow the machine?

ASTRA saved the question in the morning review queue.

Then she checked Aaron's home arrival notification, which he had chosen to share with her.

He was home.

The laboratory was safe.

For the moment, that was enough.

Tomorrow, she would discover he had left something out.

And he would learn that a person who loved him could be much harder to fool than a receiver calibrated against the wrong sky.
